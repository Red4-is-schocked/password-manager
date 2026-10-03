import os
import json
import base64
import getpass
import hashlib

from cryptography.fernet import Fernet, InvalidToken


VAULT_FILE = "vault.enc"
SALT_SIZE = 16
ITERATIONS = 600_000


def derive_key(password, salt):
    key = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt,
        ITERATIONS,
        dklen=32
    )

    return base64.urlsafe_b64encode(key)


def create_vault():
    print("\n=== Create Password Vault ===")

    password = getpass.getpass("Create master password: ")
    confirm = getpass.getpass("Confirm master password: ")

    if password != confirm:
        print("Passwords don't match.")
        return False

    if len(password) < 8:
        print("Master password must be at least 8 characters.")
        return False

    salt = os.urandom(SALT_SIZE)

    key = derive_key(password, salt)
    fernet = Fernet(key)

    data = {
        "entries": []
    }

    encrypted = fernet.encrypt(
        json.dumps(data).encode()
    )

    # File format:
    # [16-byte salt][encrypted data]
    with open(VAULT_FILE, "wb") as file:
        file.write(salt)
        file.write(encrypted)

    print("Vault created successfully.\n")
    return True


def unlock_vault():
    password = getpass.getpass("Master password: ")

    try:
        with open(VAULT_FILE, "rb") as file:
            vault = file.read()

        if len(vault) <= SALT_SIZE:
            print("Vault file is corrupted.")
            return None, None, None

        # First 16 bytes = salt
        salt = vault[:SALT_SIZE]

        # Everything after salt = encrypted data
        ciphertext = vault[SALT_SIZE:]

        key = derive_key(password, salt)

        fernet = Fernet(key)

        decrypted = fernet.decrypt(ciphertext)

        data = json.loads(decrypted.decode())

        return data, key, salt

    except FileNotFoundError:
        print("Vault doesn't exist.")
        return None, None, None

    except InvalidToken:
        print("Wrong master password.")
        return None, None, None

    except (json.JSONDecodeError, UnicodeDecodeError):
        print("Vault is corrupted.")
        return None, None, None


def save_vault(data, key, salt):
    fernet = Fernet(key)

    plaintext = json.dumps(
        data,
        indent=2
    ).encode()

    encrypted = fernet.encrypt(plaintext)

    with open(VAULT_FILE, "wb") as file:
        file.write(salt)
        file.write(encrypted)


def add_password(data):
    print("\n=== Add Password ===")

    service = input("Service: ")
    username = input("Username/email: ")
    password = getpass.getpass("Password: ")

    entry = {
        "service": service,
        "username": username,
        "password": password
    }

    data["entries"].append(entry)

    print("Password added successfully.")


def list_passwords(data):
    entries = data.get("entries", [])

    if not entries:
        print("\nVault is empty.")
        return

    print("\n=== Accounts ===")

    for i, entry in enumerate(entries, 1):
        print(
            f"{i}. {entry['service']} "
            f"- {entry['username']}"
        )


def show_password(data):
    entries = data.get("entries", [])

    if not entries:
        print("\nVault is empty.")
        return

    list_passwords(data)

    try:
        choice = int(input("\nAccount number: "))

        entry = entries[choice - 1]

        print("\n=== Account ===")
        print("Service :", entry["service"])
        print("Username:", entry["username"])
        print("Password:", entry["password"])

    except (ValueError, IndexError):
        print("Invalid choice.")


def delete_password(data):
    entries = data.get("entries", [])

    if not entries:
        print("\nVault is empty.")
        return

    list_passwords(data)

    try:
        choice = int(input("\nAccount number: "))

        deleted = entries.pop(choice - 1)

        print(
            f"Deleted account: {deleted['service']}"
        )

    except (ValueError, IndexError):
        print("Invalid choice.")


def main():
    # First launch
    if not os.path.exists(VAULT_FILE):

        if not create_vault():
            return

    # Unlock
    data, key, salt = unlock_vault()

    if data is None:
        return

    while True:

        print("""
╔══════════════════════════╗
║      PASSWORD VAULT      ║
╠══════════════════════════╣
║ 1. Add password          ║
║ 2. List accounts         ║
║ 3. Show password         ║
║ 4. Delete password       ║
║ 5. Exit                  ║
╚══════════════════════════╝
""")

        choice = input("Choice: ")

        if choice == "1":

            add_password(data)
            save_vault(data, key, salt)

        elif choice == "2":

            list_passwords(data)

        elif choice == "3":

            show_password(data)

        elif choice == "4":

            delete_password(data)
            save_vault(data, key, salt)

        elif choice == "5":

            print("Vault locked.")
            break

        else:

            print("Invalid option.")


if __name__ == "__main__":
    main()