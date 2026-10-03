# 🔐 Password Vault

A simple **local password manager** built with Python.

The project allows you to securely store and manage passwords in an **encrypted local vault**, protected by a master password.

> ⚠️ This project is designed for learning and personal use. It has not been audited as a production-grade password manager.

---

## ✨ Features

- 🔐 Encrypted password vault
- 🔑 Master password protection
- 🧂 Random cryptographic salt
- 🔒 PBKDF2-HMAC-SHA256 key derivation
- 🛡️ Fernet authenticated encryption
- ➕ Add passwords
- 📋 List stored accounts
- 👁️ Display stored passwords
- 🗑️ Delete passwords
- 🚫 Maximum of 3 failed login attempts
- 💻 Fully local — no cloud or external server
- 🌐 No internet connection required

---

## 📦 Requirements

- Python 3.9+
- `cryptography`

Install the dependency:

```bash
pip install cryptography
```

🚀 Installation

Clone the repository:
```
git clone https://github.com/Red4-is-schocked/password-vault.git
```
Enter the project directory:
```
cd password-vault
```
Install dependencies:
```
pip install cryptography
```
Run the program:
```
python3 vault.py
```
🔐 First Launch

On the first launch, the program creates a new encrypted vault.
```
=== Create Password Vault ===

Create master password:
Confirm master password:

Vault created successfully.
```
The vault is stored locally as:
```
vault.enc
```
🖥️ Menu

After unlocking the vault, you'll see:
```
╔══════════════════════════╗
║      PASSWORD VAULT      ║
╠══════════════════════════╣
║ 1. Add password          ║
║ 2. List accounts         ║
║ 3. Show password         ║
║ 4. Delete password       ║
║ 5. Exit                  ║
╚══════════════════════════╝
```
1. Add password

Store a new account:

Service: GitHub
Username/email: example@email.com
Password:
2. List accounts

Displays the services and usernames stored in the vault without revealing passwords.

3. Show password

Select an account to display its stored password.

4. Delete password

Select an account and permanently remove it from the vault.

5. Exit

Locks the vault and exits the program.

Built as a Python cybersecurity project to learn about:

Encryption
Key derivation
Secure password storage
File-based security
Python security practices
