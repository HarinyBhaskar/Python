import re, logging

logging.basicConfig(filename="phones.log", level=logging.INFO)

def validate_number(num):
    pattern = r"^\+?\d{1,3}?[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$"
    return bool(re.match(pattern, num))

if __name__ == "__main__":
    numbers = input("Enter phone numbers (comma separated): ").split(",")
    for n in numbers:
        n = n.strip()
        if validate_number(n):
            print(n, "✅ Valid")
            logging.info(f"{n} valid")
        else:
            print(n, "❌ Invalid")
            logging.warning(f"{n} invalid")
