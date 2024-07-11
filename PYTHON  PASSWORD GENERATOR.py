import random
import string

def generate_password(length, complexity):
    """Generate a random password based on the specified length and complexity."""
    # Define the character sets for different complexities
    if complexity == 1:
        chars = string.ascii_letters  # Letters only
    elif complexity == 2:
        chars = string.ascii_letters + string.digits  # Letters and digits
    elif complexity == 3:
        chars = string.ascii_letters + string.digits + string.punctuation  # Letters, digits, and special characters
    else:
        raise ValueError("Invalid complexity level. Please choose 1, 2, or 3.")
    
    # Generate the password
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    """Main function to prompt user input and display the generated password."""
    # Prompt user for the length of the password
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                raise ValueError("Length must be a positive integer.")
            break
        except ValueError as e:
            print(e)
            print("Please enter a valid number.")

    # Prompt user for the complexity level
    while True:
        try:
            complexity = int(input("Enter the complexity level (1 for letters only, 2 for letters and digits, 3 for letters, digits, and special characters): "))
            if complexity not in [1, 2, 3]:
                raise ValueError("Complexity level must be 1, 2, or 3.")
            break
        except ValueError as e:
            print(e)
            print("Please enter a valid complexity level.")

    # Generate the password
    password = generate_password(length, complexity)

    # Display the generated password
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
