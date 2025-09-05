# password_gen_cli.py
import argparse
import random
import string

def main():
    parser = argparse.ArgumentParser(description="Password Generator CLI")
    parser.add_argument("--length", type=int, default=12, help="Length of password")
    args = parser.parse_args()

    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(args.length))
    
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
