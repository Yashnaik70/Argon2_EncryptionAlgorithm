from argon2 import exceptions  # to handle password verification exceptions

# User input during login
input_username = "yash_naik"
input_password = "SuperSecretPassword123"

# Stored values (simulated database)
db_encrypted_username = encrypted_username
db_hashed_password = hashed_password

try:
    # Step 1: Verify the entered password against the hashed one
    ph.verify(db_hashed_password, input_password)
    print("Password is correct!")

    # Step 2: Decrypt the stored encrypted username
    decrypted_username = fernet.decrypt(db_encrypted_username).decode()

    # Step 3: Check if decrypted username matches input
    if decrypted_username == input_username:
        print("Username matches! Login successful.")
    else:
        print("Username mismatch!")

except exceptions.VerifyMismatchError:
    # If password verification fails
    print("Incorrect password!")
