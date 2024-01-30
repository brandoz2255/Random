import secrets
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hmac

def generate_salt():
    # Use the secrets module to generate a random salt
    return secrets.token_hex(16)

def hash_password(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        salt=salt.encode('utf-8'),
        iterations=100000,
        key_length=32
    )
    key = kdf.derive(password.encode('utf-8'))
    return key  # Return the salt and hashed password

def verify_password(provided_password, stored_salt, stored_hash):
    # Verify a provided password against a stored salt and hash
    # Perform a similar hashing process and compare the result with the stored hash
    derived_key = hash_password(provided_password, stored_salt)
    return hmac.compare_digest(derived_key, stored_hash)

