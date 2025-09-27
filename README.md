# ⚡ Worker – Allora ML Worker

This worker runs a single Allora ML model for **log-return prediction** on a chosen topic.  
It trains a **LightGBM model**, evaluates performance, and continuously submits live predictions to the **Allora Network**.

---

## 📋 Requirements

- Python **3.12+**  
- Windows 11 / WSL2 or Linux (recommended for GPU)  
- [Allora Forge Builder Kit](https://github.com/allora-network/allora-forge-builder-kit)  
- LightGBM (GPU build optional, CPU works fine)  
- Allora CLI (`allorad`) for wallet setup  

---

## 🛠 Install Dependencies

### 1. System Packages (Linux / WSL2)
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

### 5. Install allorad + Create Wallet  
(⚠️ Skip this step if you already have a wallet)

```bash
# Install allorad
curl -sSL https://raw.githubusercontent.com/allora-network/allora-chain/dev/install.sh | bash -s -- v0.12.1

```
# Create and manage your Allora wallet
```bash
allorad keys add your_wallet_name      # Create your wallet

```
```bash
allorad keys list                      # List all wallets
allorad keys show your_wallet_name -a  # Show your wallet address

```

⚠️ Save your **24-word mnemonic** and wallet address securely.  
If you already have a wallet, you can skip this step and just run the worker.

---

### 6. 🍏 MacOS Users – Install libomp

LightGBM requires `libomp` on MacOS.  
Before running your worker, install and configure it:

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

When you run it, the script will:

1. Ask for your **Allora API key**  
2. Download the **historical data**  
3. Train the **LightGBM model** (CPU by default, GPU optional if compiled)  
4. Save the `.pkl` model file  
5. Prompt you to **enter your wallet mnemonic (24 words)**  
6. Begin submitting predictions to the **Allora network** 🚀  

---

## 📊 Notes

- **GPU Training (Optional):** You must build LightGBM with CUDA/OpenCL.  
  If not compiled, the worker automatically falls back to CPU.  
- **Logs:** Training progress, metrics, and submission confirmations will print in the console.  

---


## 📜 License

This project is licensed under the MIT License.
