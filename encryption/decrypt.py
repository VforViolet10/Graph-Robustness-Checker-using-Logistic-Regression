# encryption/decrypt.py

import sys
import os
from pathlib import Path
from dotenv import load_dotenv
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.fernet import Fernet

load_dotenv()

def decrypt_file_content(encrypted_file_path: Path) -> bytes:
    private_key_pem = os.environ.get("SUBMISSION_PRIVATE_KEY")
    
    if not private_key_pem:
        raise ValueError("Missing SUBMISSION_PRIVATE_KEY in environment")

    private_key_pem = private_key_pem.replace('\\n', '\n').strip()

    private_key = serialization.load_pem_private_key(
        private_key_pem.encode(),
        password=None
    )

    with open(encrypted_file_path, "rb") as f:
        file_content = f.read()

    # First 256 bytes = RSA encrypted key
    encrypted_key = file_content[:256]
    encrypted_data = file_content[256:]

    session_key = private_key.decrypt(
        encrypted_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    cipher = Fernet(session_key)
    decrypted_data = cipher.decrypt(encrypted_data)

    return decrypted_data


def decrypt_file(input_path: Path, output_path: Path):
    data = decrypt_file_content(input_path)

    with open(output_path, "wb") as f:
        f.write(data)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python decrypt.py <file.enc>")
        sys.exit(1)

    encrypted_file = Path(sys.argv[1])
    output_file = encrypted_file.with_suffix("")

    decrypt_file(encrypted_file, output_file)
    print(f"✅ Decrypted → {output_file}")
