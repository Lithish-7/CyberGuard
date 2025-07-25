import hashlib

def check_file_integrity(filepath):
    try:
        with open(filepath, "rb") as f:
            file_data = f.read()
            sha256_hash = hashlib.sha256(file_data).hexdigest()
        print(f"SHA256 Hash: {sha256_hash}")
    except FileNotFoundError:
        print("File not found!")
