import hashlib
import sys
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

def load_private_key():
    with open("private.pem", "rb") as f:
        return serialization.load_pem_private_key(f.read(), password=None)

def load_public_key():
    with open("public.pem", "rb") as f:
        return serialization.load_pem_public_key(f.read())

#hash function
def hash_file(filepath):
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(4096):
            sha256.update(chunk)
    return sha256.digest()  # bytes olarak dönüyor

#sign function
def sign_file(filepath):
    private_key = load_private_key()
    file_hash = hash_file(filepath)

    signature = private_key.sign(
        file_hash,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    with open(filepath + ".sig", "wb") as f:
        f.write(signature)

    print("Signature oluşturuldu:", filepath + ".sig")

#werify function
def verify_file(filepath, sigpath):
    public_key = load_public_key()
    file_hash = hash_file(filepath)

    with open(sigpath, "rb") as f:
        signature = f.read()

    try:
        public_key.verify(
            signature,
            file_hash,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        print("Doğrulama BAŞARILI")
    except Exception:
        print("Doğrulama BAŞARISIZ")

# CLI entry point and usage message
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage:")
        print("  python trustverify.py hash <file>")
        print("  python trustverify.py sign <file>")
        print("  python trustverify.py verify <file> <sig>")
        sys.exit(1)

    command = sys.argv[1]

    if command == "hash":
        file = sys.argv[2]
        print("Hash:", hash_file(file).hex())
    elif command == "sign":
        file = sys.argv[2]
        sign_file(file)
    elif command == "verify":
        if len(sys.argv) < 4:
            print("Usage: python trustverify.py verify <file> <sig>")
            sys.exit(1)
        file = sys.argv[2]
        sig = sys.argv[3]
        verify_file(file, sig)
    else:
        print("Unknown command:", command)

  
