import re, logging

logging.basicConfig(filename="passwords.log", level=logging.INFO)

def check_password(pw):
    if (len(pw) >= 8 and
        re.search(r"[A-Z]", pw) and
        re.search(r"[a-z]", pw) and
        re.search(r"\d", pw) and
        re.search(r"[!@#$%^&*]", pw)):
        return True
    return False

if __name__ == "__main__":
    pw = input("Enter a password: ")
    if check_password(pw):
        print("✅ Strong password")
        logging.info(f"Strong: {pw}")
    else:
        print("❌ Weak password")
        logging.warning(f"Weak: {pw}")
