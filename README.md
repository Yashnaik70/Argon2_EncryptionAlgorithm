# Argon2_EncryptionAlgorithm

This is a simple Python script demonstrating how to securely store user credentials using Argon2 for password hashing and AES (via Fernet) for encrypting sensitive user information like usernames.

---

## 🔐 Features

- Encrypts the username using `cryptography.fernet` (AES-based)
- Hashes the password using `argon2` (argon2-cffi)
- Displays encrypted username, hashed password, and encryption key
- Demonstrates modern security practices for storing credentials

---

## 📦 Requirements

Install the necessary Python libraries:

```bash
pip install cryptography argon2-cffi
```

---

## 🚀 How to Run

1. Save the script as `secure_user_store.py`
2. Run the script:

```bash
python secure_user_store.py
```

3. Enter a username and password when prompted.

---

## 📘 Example Output

```
Enter The Username : yashnaik
Enter The Password : strongpass123

Encrypted Username: gAAAAABg...

Hashed Password: $argon2id$v=19$m=65536,t=3,p=4$...

Fernet Key (Keep safe!): 2jR1Jz...
```

---

## ⚠️ Notes

- The **Fernet key** is required to decrypt the username. Store it securely.
- The **password hash** is one-way and cannot be reversed (for verification only).
- This is a demonstration script; do not hardcode or expose secrets in production.

---

## 👨‍💻 Author

**Yash Naik**  
Cybersecurity Student | Python Developer  
[GitHub Profile](https://github.com/Yashnaik70)

---

## 📜 License

This project is intended for learning and demonstration purposes only.
