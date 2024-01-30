import random

import string

  

def generate_password(length=12, use_digits=True, use_special_chars=True):
    uppercase = string.ascii_uppercase

    lowercase = string.ascii_lowercase

    digits = string.digits if use_digits else ""

    special_chars = string.punctuation if use_special_chars else ""
  
    characters = uppercase + lowercase + digits + special_chars
    if not characters:
     raise ValueError("Please enable at least one character set (letters, digits, or special characters).")

  

 # Generate the password

 
    
    password = "".join(random.choice(characters) for _ in range(length))
    return password


password = generate_password(length=16, use_digits=True, use_special_chars=True)
print("Generated Password:", password)