#!/usr/bin/env python3
import argparse
import asyncio
import os
import cloudpickle
import lightgbm as lgb
import numpy as np
import pandas as pd
from collections import deque
from sklearn.model_selection import ParameterSampler
from allora_forge_builder_kit import AlloraMLWorkflow, get_api_key
from allora_sdk.worker import AlloraWorker

# === Topic mapping (BTCUSD, Topic 69) ===
TOPIC_ID = 69
TICKER = "btcusd"

# === Hyperparameter search space ===
PARAM_SPACE = {
    "max_depth": [2, 3, 4, 5, 6, 7, 8, 9, 10],
    "learning_rate": [0.0001, 0.001, 0.01, 0.1],
    "reg_lambda": [1, 10, 100, 1000],
    "min_child_weight": [10, 100, 1000],
    "max_bin": [8, 16, 32, 64],
    "num_leaves": [4, 8, 16, 32, 64],
    "colsample_bytree": [0.5, 0.7, 0.9, 1.0],
}
N_RANDOM_SAMPLES = 50
TOP_K_MODELS = 3       # ensemble size
PREDICT_FILE = f"predict_{TICKER}_topic{TOPIC_ID}.pkl"


def corr_eval_metric(y_true, y_pred):
    corr = np.corrcoef(y_true, y_pred)[0, 1]
    return "corr", corr, True


def train_and_save(api_key):
    print(f"[{TICKER.upper()}] 🚀 Training Topic {TOPIC_ID} predictor (CPU only)")

    workflow = AlloraMLWorkflow(
        data_api_key=api_key,
        tickers=[TICKER],
        hours_needed=5 * 24,
        number_of_input_candles=12,
        target_length=24,
    )

    X_train, y_train, X_val, y_val, X_test, y_test = workflow.get_train_validation_test_data(
        from_month="2023-01", validation_months=3, test_months=3
    )
    feature_cols = [c for c in X_train.columns if "feature" in c]

    results = []
    random_params = list(ParameterSampler(PARAM_SPACE, n_iter=N_RANDOM_SAMPLES, random_state=42))

    for params in random_params:
        model = lgb.LGBMRegressor(n_estimators=1000, device_type="cpu", **params)
        model.fit(
            X_train[feature_cols],
            y_train,
            eval_set=[(X_val[feature_cols], y_val)],
            eval_metric=corr_eval_metric,
            callbacks=[lgb.early_stopping(stopping_rounds=100, verbose=False)],
        )

        val_preds = model.predict(X_val[feature_cols])
        test_preds = model.predict(X_test[feature_cols])

        val_corr = np.corrcoef(y_val, val_preds)[0, 1]
        val_dir = np.mean((np.sign(val_preds) == np.sign(y_val)).astype(int))
        test_corr = np.corrcoef(y_test, test_preds)[0, 1]

        score = 0.7 * val_corr + 0.3 * val_dir

        results.append({
            "params": params,
            "n_estimators": getattr(model, "best_iteration_", 1000),
            "val_corr": val_corr,
            "val_dir": val_dir,
            "test_corr": test_corr,
            "score": score,
        })

    # Sort by score
    results_df = pd.DataFrame(results).sort_values(by="score", ascending=False)
    print(f"[{TICKER.upper()}] Top results:\n", results_df.head(5))

    # Select top-K
    top_models = []
    for _, row in results_df.head(TOP_K_MODELS).iterrows():
        model = lgb.LGBMRegressor(
            n_estimators=int(row["n_estimators"]),
            device_type="cpu",
            **row["params"]
        )
        model.fit(
            pd.concat([X_train[feature_cols], X_val[feature_cols], X_test[feature_cols]]),
            pd.concat([y_train, y_val, y_test]),
        )
        top_models.append(model)

    # Rolling smoother
    last_preds = deque(maxlen=5)

    def predict() -> float:
        live_features = workflow.get_live_features(TICKER)
        preds = np.mean([m.predict(live_features) for m in top_models])
        last_preds.append(preds)
        smoothed = np.mean(last_preds)
        return float(np.clip(smoothed, -0.1, 0.1))  # cap extreme outliers

    with open(PREDICT_FILE, "wb") as f:
        cloudpickle.dump(predict, f)
    print(f"[{TICKER.upper()}] 💾 Pickle saved: {PREDICT_FILE}")


async def run_worker(api_key):
    if not os.path.exists(PREDICT_FILE):
        print(f"[{TICKER.upper()}] ❌ No pickle found, you must train first.")
        return

    with open(PREDICT_FILE, "rb") as f:
        predict_fn = cloudpickle.load(f)

    worker = AlloraWorker(
        predict_fn=predict_fn,
        api_key=api_key,
        topic_id=TOPIC_ID,
    )

    print(f"[{TICKER.upper()}] 🛰️ Starting worker → Topic {TOPIC_ID}")
    async for result in worker.run():
        if isinstance(result, Exception):
            print(f"[{TICKER.upper()}] error: {str(result)}")
        else:
            print(f"[{TICKER.upper()}] ✅ Prediction submitted: {result.prediction}")


async def main(retrain=False):
    api_key = get_api_key()

    if retrain or not os.path.exists(PREDICT_FILE):
        train_and_save(api_key)
    else:
        print(f"[{TICKER.upper()}] ⏭️ Skipping training, using existing {PREDICT_FILE}")

    await run_worker(api_key)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--retrain", action="store_true", help="Force retraining even if pickle exists")
    args = parser.parse_args()

    asyncio.run(main(retrain=args.retrain))
