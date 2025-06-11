from argon2 import PasswordHasher  # for secure password hashing
from cryptography.fernet import Fernet  # for encrypting the username

ph = PasswordHasher()  # create password hasher instance
fernet_key = Fernet.generate_key()  # generate secret encryption key
fernet = Fernet(fernet_key)  # initialize Fernet with the key

username = input("Enter The Username : ")  # get username input
password = input("Enter The Password : ")  # get password input

encrypted_username = fernet.encrypt(username.encode())  # encrypt the username

hashed_password = ph.hash(password)  # hash the password securely

print("\nEncrypted Username:", encrypted_username.decode())  # show encrypted username

print("\nHashed Password:", hashed_password)  # show hashed password

print("\nFernet Key (Keep safe!):", fernet_key.decode())  # show Fernet key (for decryption)
