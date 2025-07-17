# 💀 Ransomware Simulator (Safe Educational Tool)

This Python script simulates how ransomware encrypts `.txt` files using AES. It's for educational use only — no files are deleted or harmed.

## 🔐 How It Works

- Encrypts files in `target_files/` folder
- AES key is saved to `key.key`
- `decryptor.py` can decrypt files using the saved key

## 🚀 Run It

```bash
pip install -r requirements.txt
python encryptor.py   # To simulate attack
python decryptor.py   # To recover files
