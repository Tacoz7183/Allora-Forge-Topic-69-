# ⚡ Worker 69 – Allora ML Worker

This worker runs a single **Allora ML model** for log-return prediction on **Topic 69**.  
It trains a **LightGBM model**, evaluates performance, and continuously submits live predictions to the Allora network.

---

## 📂 Clone Repository

```bash
git clone https://github.com/Tacoz7183/Allora-Forge-Topic-69-.git
cd Allora-Forge-Topic-69-
```

---

## 📋 Requirements

- Python **3.12+**
- **Windows 11 / WSL2** or **Linux** (recommended for GPU)
- Allora Forge Builder Kit
- LightGBM (GPU build optional, CPU works fine)

Dependencies are in `requirements.txt`:

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

## ⚙️ Environment Setup

### Linux / WSL
```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
export ALLORA_API_KEY=your_api_key_here
```

### Windows (cmd)
```bat
python -m venv venv
venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
set ALLORA_API_KEY=your_api_key_here
```

### Windows (PowerShell)
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
$env:ALLORA_API_KEY="your_api_key_here"
```

---

## 🚀 Running Worker 69

```bash
python worker69.py
```

---

## ▶️ Run in Background

Using `screen` (Linux/WSL):
```bash
screen -S worker69
python worker69.py
# Detach with CTRL+A then D
```

Using `nohup`:
```bash
nohup python worker69.py > worker69.log 2>&1 &
```

---

## 🛠️ Troubleshooting

- **API Key Missing** → Ensure `ALLORA_API_KEY` is set correctly.  
- **No GPU Detected** → LightGBM will fall back to CPU automatically.  
- **Dependency Errors** → Run `pip install -r requirements.txt --force-reinstall`.  

---

✅ Your Worker is now ready to train, evaluate, and submit predictions for **Topic 69**.
