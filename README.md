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
git clone https://github.com/YOUR_USERNAME/password-vault.git
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

🔑 Security

The master password is never stored directly.

A random 16-byte salt is generated when the vault is created.

The encryption key is derived using:

PBKDF2-HMAC-SHA256
600,000 iterations
32-byte derived key

The derived key is then used with Fernet authenticated encryption.

The vault file has the following structure:

┌──────────────────┬─────────────────────────────┐
│  16-byte SALT    │     ENCRYPTED VAULT DATA   │
└──────────────────┴─────────────────────────────┘

Passwords are therefore not stored as plaintext inside vault.enc.

🚫 Failed Login Attempts

The vault allows a maximum of 3 incorrect master-password attempts per program launch.

Example:

Master password:
Wrong master password. 2 attempt(s) remaining.

Master password:
Wrong master password. 1 attempt(s) remaining.

Master password:
Too many failed attempts.
Vault locked.
------------------------------------------------------------
Important considerations include:

Keep your master password strong and unique.
Never commit vault.enc to a public GitHub repository.
Never commit passwords or secrets to Git.
Keep backups of your vault in a secure location.
Losing the master password means the encrypted data cannot normally be decrypted.
The project has not undergone an independent security audit.
🛠️ Technologies
Python
cryptography
PBKDF2-HMAC-SHA256
Fernet
JSON
Git / GitHub
📚 Future Improvements

Possible features for future versions:

 Password generator
 Search accounts
 Edit existing passwords
 Change master password
 Automatic vault locking
 Clipboard integration with automatic clearing
 Password strength checker
 Account categories
 Backup and restore
 GUI interface
 Secure deletion improvements
 Authentication rate limiting across restarts
👨‍💻 Author

Your Name

Built as a Python cybersecurity project to learn about:

Encryption
Key derivation
Secure password storage
File-based security
Python security practices
