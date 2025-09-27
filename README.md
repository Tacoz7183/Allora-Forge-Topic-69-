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

## ⚙️ Environment Setup

Set your Allora API key (replace with your real key):
set ALLORA_API_KEY=your_api_key_here      # On Windows (cmd)
export ALLORA_API_KEY=your_api_key_here   # On Linux / WSL

##  🚀 Running Topic 69

python worker69.py

