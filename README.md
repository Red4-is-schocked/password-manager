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
