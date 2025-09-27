# ⚡ Worker 69 – Allora ML Worker

This worker runs a single Allora ML model for log-return prediction on **Topic 69**.  
It trains a LightGBM model, evaluates performance, and continuously submits live predictions to the Allora network.

---

## 📋 Requirements

- Python 3.12+  
- Windows 11 / WSL2 or Linux (recommended for GPU)  
- Allora Forge Builder Kit  
- LightGBM (CPU works fine; GPU optional if compiled)  

Dependencies are already in `requirements.txt`:

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

## 📦 Clone and Run

```bash
git clone https://github.com/Tacoz7183/allora-forge.git
cd allora-forge

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate   # Activate venv

# Install dependencies
pip install -r requirements.txt

# Run the worker
python worker69.py
```

---

## 🚀 Running Worker 69

```bash
python worker69.py
```

When you run it, the script will:

1. Ask for your Allora API key  
2. Download the Historical Data  
3. Train the model  
4. Then prompt you to enter your wallet mnemonic (24 words)  
5. Begin submitting predictions to the Allora network  

---

## 🔐 Create and Manage Your Allora Wallet with `allorad`

If you **don’t already have an Allora wallet**, install `allorad` and create one:

```bash
curl -sSL https://raw.githubusercontent.com/allora-network/allora-chain/dev/install.sh | bash -s -- v0.12.1

# Create a new wallet
allorad keys add your_wallet_name

# List wallets
allorad keys list

# Show wallet address
allorad keys show your_wallet_name -a
```

If you **already have a wallet**, you don’t need to run these commands.  
Just start the worker (`python worker69.py`) and it will ask you for your mnemonic automatically.

---

## 📝 Summary

The script will:

- Ask for your Allora API key  
- Download historical data  
- Train the model  
- Prompt you for your wallet mnemonic (24 words)  
- Submit predictions live to the Allora network for Topic-69 🚀  

---
