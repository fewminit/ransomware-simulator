import os
from Crypto.Cipher import AES

def unpad(data):
    return data.rstrip(b' ')

def decrypt_file(filepath, key):
    with open(filepath, 'rb') as f:
        encrypted_data = f.read()

    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_data = unpad(cipher.decrypt(encrypted_data))

    with open(filepath, 'wb') as f:
        f.write(decrypted_data)

def main():
    target_dir = "target_files"

    try:
        with open("key.key", "rb") as key_file:
            key = key_file.read()
    except FileNotFoundError:
        print("❌ Key file not found. Cannot decrypt.")
        return

    print("🔓 Decrypting files in folder:", target_dir)
    for filename in os.listdir(target_dir):
        if filename.endswith(".txt"):
            filepath = os.path.join(target_dir, filename)
            decrypt_file(filepath, key)
            print(f"  🔓 {filename} decrypted")

    print("\n✅ Files restored Thanks to akash.")

if __name__ == "__main__":
    main()
