import argparse
import random
import string

def get_args():
    parser = argparse.ArgumentParser(description="Random Password Generator")
    parser.add_argument("-l", "--length", type=int, help="Length of the password")
    parser.add_argument("-u", "--uppercase", action="store_true", help="Include uppercase letters")
    parser.add_argument("-lc", "--lowercase", action="store_true", help="Include lowercase letters")
    parser.add_argument("-d", "--digits", action="store_true", help="Include digits")
    parser.add_argument("-s", "--special", action="store_true", help="Include special characters")
    args = parser.parse_args()
    
    return args

def interactive_prompt():
    length = int(input("Enter the length of the password: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'
    
    if not (use_uppercase or use_lowercase or use_digits or use_special):
        print("Error: No character set selected. Please select at least one character set.")
        exit(1)
    
    return length, use_uppercase, use_lowercase, use_digits, use_special

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    character_pool = ""
    
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation
    
    if not character_pool:
        raise ValueError("Character pool is empty. At least one character set must be specified.")
    
    secure_random = random.SystemRandom()
    password = ''.join(secure_random.choice(character_pool) for _ in range(length))
    
    return password

def main():
    args = get_args()
    
    if args.length is None:
        length, use_uppercase, use_lowercase, use_digits, use_special = interactive_prompt()
    else:
        length = args.length
        use_uppercase = args.uppercase
        use_lowercase = args.lowercase
        use_digits = args.digits
        use_special = args.special
    
        if not (use_uppercase or use_lowercase or use_digits or use_special):
            print("Error: No character set selected. Please select at least one character set.")
            exit(1)
    
    password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()

