# Allora-Forge
The Allora Model Forge is the hub for monetization of machine learning models. Compete alongside top talent in AI, create models with real impact, and earn rewards &amp; recognition within the Allora ecosystem and beyond.

# ⚡ Worker 69 – Allora ML Worker

This worker runs a **single Allora ML model** for log-return prediction on topic **69**.  
It trains a LightGBM model, evaluates performance, and continuously submits live predictions to the Allora network.

---

## 📋 Requirements

- Python **3.12+**
- Windows 11 / WSL2 or Linux (recommended for GPU)
- [Allora Forge Builder Kit](https://github.com/allora-network/allora-forge-builder-kit)  
- LightGBM (GPU build optional, CPU works fine)  

Dependencies are already in `requirements.txt`:

```txt
git+https://github.com/allora-network/allora-forge-builder-kit.git
allora_sdk>=1.0.5
lightgbm
scikit-learn
pandas
numpy
matplotlib
dill
cloudpickle

👉 Install everything into a virtual environment:

python -m venv venv
venv\Scripts\activate   # On Windows
# OR
source venv/bin/activate   # On Linux / WSL

pip install -r requirements.txt
⚙️ Environment

Export your Allora API key (from your wallet):

set ALLORA_API_KEY=your_api_key_here   # On Windows (cmd)
export ALLORA_API_KEY=your_api_key_here   # On Linux / WSL

▶️ Run Worker 69

Start the worker:

python worker69.py


The script will:

Load historical candles for the selected asset.

Train a LightGBM regressor (force_col_wise=True for efficiency).

Evaluate validation + test data.

Retrain on all data.

Start submitting live predictions to topic 69.
