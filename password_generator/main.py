import random 
import argparse

def generate_password(length:int, special_chars:bool, numbers:bool, letters:bool, capital:bool) -> str:
    """Generate a password with the given length and special characters."""

    
    letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    special_chars = "!@#$%^&*()_-=+~,./[]<>?"

    password = ""

    elements = [letters, numbers, special_chars]

    if special_chars == False:
        elements.remove(special_chars)
    if numbers == False:
        elements.remove(numbers)
    if letters == False:
        elements.remove(letters)
    for i in range(length):
        if capital == True and i == 0:
            password += random.choice(letters.upper())
        else:
            password += random.choice(random.choice(elements))
    return password



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a password.")
    parser.add_argument("length", type=int, help="Length of the password")
    parser.add_argument("-s", "--special-chars", action="store_true", help="Include special characters")
    parser.add_argument("-n", "--numbers", action="store_true", help="Include numbers")
    parser.add_argument("-l", "--letters", action="store_true", help="Include letters")
    parser.add_argument("-c", "--capital", action="store_true", help="Start with a capital letter")
    args = parser.parse_args()
    password = generate_password(args.length, args.special_chars, args.numbers, args.letters, args.capital)
    
    print(password)
    