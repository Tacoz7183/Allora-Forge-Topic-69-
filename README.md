# ⚡ Worker – Allora ML Worker

This worker runs a single Allora ML model for log-return prediction on a chosen topic.  
It trains a LightGBM model, evaluates performance, and continuously submits live predictions to the Allora network.

---

## 📋 Requirements

- Python 3.12+  
- Windows 11 / WSL2 or Linux (recommended for GPU)  
- Allora Forge Builder Kit  
- LightGBM (GPU build optional, CPU works fine)  

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

## 🛠 Install Dependencies from Scratch

### 1. System Packages
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y git python3 python3-venv python3-pip build-essential cmake
```

### 2. Clone Repository
```bash
git clone https://github.com/Tacoz7183/allora-forge.git
cd allora-forge
```

### 3. Python Environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
```

### 4. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 5. Install allorad (Skip this step if you already have a wallet)
```bash
curl -sSL https://raw.githubusercontent.com/allora-network/allora-chain/dev/install.sh | bash -s -- v0.12.1
```

---

## 🔐 Create and Manage Your Allora Wallet with allorad

If you don’t have an Allora wallet yet:

```bash
allorad keys add your_wallet_name    # Create your wallet
allorad keys list                    # List all wallets
allorad keys show your_wallet_name -a # Show your wallet address
```

If you already have a wallet, you can skip this and just run the worker.

---

## 🚀 Running Worker

```bash
python worker.py
```

The script will:

1. Ask for your Allora API key  
2. Download the historical data  
3. Train the model  
4. Save the `.pkl` model file  
5. Prompt you to enter your wallet mnemonic (24 words)  
6. Begin submitting predictions to the Allora network 🚀 

---
