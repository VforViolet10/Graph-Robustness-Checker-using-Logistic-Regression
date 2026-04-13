# encryption/encrypt.py

import sys
import os
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.fernet import Fernet

def encrypt_file(file_path):
    # Load public key
    key_path = os.path.join(os.path.dirname(__file__), "public_key.pem")

    with open(key_path, "rb") as f:
        public_key = serialization.load_pem_public_key(f.read())

    # Generate session key
    session_key = Fernet.generate_key()
    cipher = Fernet(session_key)

    # Read file
    with open(file_path, "rb") as f:
        data = f.read()

    # Encrypt data
    encrypted_data = cipher.encrypt(data)

    # Encrypt session key using RSA
    encrypted_key = public_key.encrypt(
        session_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Save combined file
    output_file = file_path + ".enc"
    with open(output_file, "wb") as f:
        f.write(encrypted_key)
        f.write(encrypted_data)

    print(f"✅ Encrypted → {output_file}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python encrypt.py <file>")
    else:
        encrypt_file(sys.argv[1])
