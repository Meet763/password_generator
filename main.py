import random
import string

def generate_password(length, characters, include_uppercase, include_digits, include_special):
    # Define the possible character sets
    lowercase = string.ascii_lowercase if include_uppercase else ''
    uppercase = string.ascii_uppercase if include_uppercase else ''
    digits = string.digits if include_digits else ''
    special = string.punctuation if include_special else ''
    
    # Combine the character sets into one string
    all_chars = lowercase + uppercase + digits + special
    
    if not all_chars:
        raise ValueError("No character types selected. At least one type must be included.")
    
    # Generate the password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password


length = int(input("Enter the length of password: "))

include_alpha = input("Do you want to include alphabetical characters (y/n)? ").lower() == "y"
if include_alpha:
    # If yes, ask if they want lowercase, uppercase, or both
    include_lowercase = input("Do you want to include lowercase characters (y/n)? ").lower() == "y"
    include_uppercase = input("Do you want to include uppercase characters (y/n)? ").lower() == "y"
else:
    # If no, set both to False
    include_lowercase = False
    include_uppercase = False

include_digits = input("do you want to add numbers (y/n)? ").lower() == "y"
include_special = input("do you want to add special characters (y/n)? ").lower() == "y"

password = generate_password(20, include_uppercase, include_lowercase, include_digits, include_special)
print(f"Generated password: {password}")
