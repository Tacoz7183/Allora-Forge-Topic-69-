# ⚡Allora ML Worker

This worker runs a single Allora ML model for testing.
It trains a LightGBM model, evaluates performance, and continuously submits live predictions to the Allora network.

NOTE: FORGE-WHITELIST Depends on the performance of your model. 

---

## 📋 Requirements
 
- Windows 11 / WSL2 or Linux
- Allora Wallet  
- Allora API Key  

---

## 🛠 Install Dependencies

###  🔑Get Allora API Key  
This gives you access to OHLCV (open, high, low, close, volume) candle data through the workflow.  

To get your API key:  
👉 Go to [Allora Developer Portal](https://developer.allora.network/), create an account, and generate a new API key.  

---

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

### 3. Python Environment and Install Python Dependencies
```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Install allorad (Skip this step if you already have a wallet)
```bash
curl -sSL https://raw.githubusercontent.com/allora-network/allora-chain/dev/install.sh | bash -s -- v0.12.1
```

#### a. Create your wallet
```bash
allorad keys add your_wallet_name
```

#### b. List all wallets
```bash
allorad keys list
```

#### c. Show your wallet address
```bash
allorad keys show your_wallet_name -a
```

⚠️ Save your 24-word mnemonic and wallet address securely.  
If you already have a wallet, you can skip this step and just run the worker.

---

### 5. 🍏 MacOS Users – Install libomp
LightGBM requires libomp on MacOS. Before running your worker, install and configure it:

```bash
# Install libomp
brew install libomp

# Set environment variables (add to your ~/.zshrc or ~/.bashrc)
export LDFLAGS="-L/opt/homebrew/opt/libomp/lib"
export CPPFLAGS="-I/opt/homebrew/opt/libomp/include"
export PATH="/opt/homebrew/opt/libomp/bin:$PATH"

# Reload your shell config
source ~/.zshrc   # or source ~/.bashrc
```

Now you can run:
```bash
python worker.py
```

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
