import logging
import string
from itertools import product

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    # User input for password length
    length = int(input("Enter password length: "))

    # Ask what characters to include
    choice = input("Use (a) letters only, (b) digits only, (c) letters+digits? ").lower()

    if choice == 'a':
        chars = string.ascii_letters
    elif choice == 'b':
        chars = string.digits
    else:
        chars = string.ascii_letters + string.digits

    logging.info(f"Using {len(chars)} characters for password generation.")

    # Generate all combinations
    passwords = product(chars, repeat=length)

    print("\nSample generated passwords:")
    for i, p in enumerate(passwords, start=1):
        pwd = ''.join(p)
        if i <= 20:   # show only first 20 to avoid overload
            print(pwd)
        if i % 1000000 == 0:   # log progress every million
            logging.info(f"Generated {i} passwords so far...")

    logging.info(f"Finished generating all possible {len(chars) ** length} passwords.")

if __name__ == "__main__":
    main()
