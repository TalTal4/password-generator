import random
import string

def generate_password(length, include_lowercase, include_uppercase, include_digits, include_symbols):
    # Define the character sets based on user input
    character_sets = []
    if include_lowercase:
        character_sets.append(string.ascii_lowercase)
    if include_uppercase:
        character_sets.append(string.ascii_uppercase)5
    if include_digits:
        character_sets.append(string.digits)
    if include_symbols:
        character_sets.append("!@#$%^&*()_+-=[]{};:,.<>/?")

    # Combine all character sets
    all_chars = "".join(character_sets)

    # Generate a random password
    password = "".join(random.sample(all_chars, length))

    return password

# Prompt the user for desired character sets
length = int(input("Enter the desired password length: "))
include_lowercase = input("Include lowercase letters? (y/n): ").lower() == "y"
include_uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
include_digits = input("Include digits? (y/n): ").lower() == "y"
include_symbols = input("Include symbols? (y/n): ").lower() == "y"

# Generate the password
generated_password = generate_password(length, include_lowercase, include_uppercase, include_digits, include_symbols)
print("Generated Password:", generated_password)