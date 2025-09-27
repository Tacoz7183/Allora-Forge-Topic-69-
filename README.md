# ⚡ Allora Forge Worker

This worker runs a single Allora ML model for log-return prediction on a chosen topic.  
It trains a LightGBM model, evaluates performance, and continuously submits live predictions to the Allora network.

---

## 📋 Requirements

- Python **3.12+**
- Windows 11 / WSL2 or Linux (recommended for GPU users)
- Allora Forge Builder Kit
- LightGBM (CPU build works fine, GPU optional)

All dependencies are listed in `requirements.txt`:

```
git+https://github.com/allora-network/allora-forge-builder-kit.git
allora_sdk>=1.0.5
lightgbm
scikit-learn
pandas
numpy
matplotlib
dill
cloudpickle
```

---

## ⚙️ Installation (from scratch)

1. **Clone the repo**
   ```bash
   git clone https://github.com/Tacoz7183/allora-forge.git
   cd allora-forge
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux / WSL
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify Python & pip**
   ```bash
   python --version
   pip --version
   ```

5. **Install `allorad` (Skip this step if you already have a wallet)**
   ```bash
   curl -sSL https://raw.githubusercontent.com/allora-network/allora-chain/dev/install.sh | bash -s -- v0.12.1
   ```
   Check installation:
   ```bash
   allorad version
   ```

---

## 🔐 Create and Manage Your Allora Wallet with `allorad`

If you **don’t have an Allora wallet yet**, run these commands:

```bash
allorad keys add your_wallet_name        # Create a new wallet
allorad keys list                        # Show all wallets stored locally
allorad keys show your_wallet_name -a    # Display your wallet address
```

👉 This will generate a **24-word mnemonic phrase**.  
⚠️ Save it securely — it’s the only way to recover your wallet.

---

If you **already have a wallet**:  
➡️ You can skip creating a new one.  
When you run the worker, it will prompt you for your **24-word mnemonic** automatically.

---

## 📦 Clone and Run

```bash
git clone https://github.com/Tacoz7183/allora-forge.git
cd allora-forge
python -m venv venv
source venv/bin/activate   # Linux / WSL
pip install -r requirements.txt
python worker.py
```

---

## 🚀 Running Worker

```bash
python worker.py
```

When you run it, the script will:

1. Ask for your **Allora API key**  
2. Download the **historical data**  
3. Train the model with LightGBM (CPU by default)  
4. Save the trained `.pkl` model file  
5. Prompt you to enter your **wallet mnemonic (24 words)**  
6. Begin **submitting predictions** to the Allora network 🚀
