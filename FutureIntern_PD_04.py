
import random #library
import string #library

def generate_password(length, include_uppercase, include_lowercase, include_digits, include_special):
    # Choices uppercase, lowercase, digits, punctuation
    characters = ''
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    # To check that user has selected atleast one type
    if not characters:
        print("Error: You must select at least one character type!")
        return None

    password = ''.join(random.choice(characters) for i in range(length))
    return password
while True:
    # Take input from the user
    length = int(input("Enter the desired length of the password: "))
    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_special = input("Include special characters? (y/n): ").lower() == 'y'


    password = generate_password(length, include_uppercase, include_lowercase, include_digits, include_special)

    # Display the Password
    if password:
        print("Generated password:", password)
    x=input("Are you satisfied with the password[Y/N]: ").lower()
    if x== "y":
        print("Thank you for using the generator!")
        break
    elif x=="n":
        print("Restarting the program.........")
        continue
    else:
        print("Invalid choice!!!")
        break