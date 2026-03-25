# TrustVerify 🔐

A CLI Tool for File Integrity and Digital Signature Verification

## 📌 Project Description

TrustVerify is a Python-based Command Line Interface (CLI) tool that ensures:

* File integrity using **SHA-256 hashing**
* Authentication using **RSA digital signatures**

It allows a sender to sign a file and a receiver to verify that:

* The file has not been modified
* The file comes from a trusted source
  
## ⚙️ Technologies Used

* Python 3
* `hashlib` (for SHA-256 hashing)
* `cryptography` library (for RSA encryption and signatures)

## 🔑 Key Generation

Before using the tool, generate RSA keys:

```bash
python keygen.py
```

This will create:

* `private.pem` → used for signing
* `public.pem` → used for verification

## 🚀 Usage

### 1️⃣ Hash a file

```bash
python trustverify.py hash test.txt
```

Output:

```
Hash: <sha256 hash value>
```

---

### 2️⃣ Sign a file

```bash
python trustverify.py sign test.txt
```

Output:

```
Signature oluşturuldu: test.txt.sig
```

This creates:

```
test.txt.sig
```
### 3️⃣ Verify a file

```bash
python trustverify.py verify test.txt test.txt.sig
```

Output (if valid):

```
Doğrulama BAŞARILI
```

Output (if modified):

```
Doğrulama BAŞARISIZ
```
## 🔍 How It Works

1. The file is hashed using SHA-256
2. The hash is signed using the private RSA key
3. The receiver verifies the signature using the public key
   
## 🔐 Security Concepts

### Hashing

A hash function converts data into a fixed-size value.
Any small change in the file produces a completely different hash.

### Digital Signature

The sender signs the hash using a private key.
The receiver verifies it using the public key.

### RSA

RSA is an asymmetric encryption algorithm using:

* Public key (shared)
* Private key (secret)

## 📁 Project Structure

```
project/
│
├── trustverify.py
├── keygen.py
├── private.pem
├── public.pem
├── test.txt
└── test.txt.sig
```

## ✅ Features

* File hashing (SHA-256)
* Digital signature generation
* Signature verification
* CLI-based interaction


## 🎯 Conclusion

This project demonstrates how cryptographic primitives like hashing and digital signatures can be combined to ensure:

* Data integrity
* Authenticity
* Security in communication

---
