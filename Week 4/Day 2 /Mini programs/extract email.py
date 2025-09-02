import re
import logging

# Setup logging
logging.basicConfig(
    filename="emails.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def extract_emails(text: str):
    """Extract all emails from input text using regex"""
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}"
    return re.findall(pattern, text)

if __name__ == "__main__":
    user_input = input("Enter some text with emails: ")
    emails = extract_emails(user_input)

    if emails:
        print("✅ Emails found:")
        for e in emails:
            print(" -", e)
        logging.info(f"Extracted emails: {emails}")
    else:
        print("❌ No emails found")
        logging.warning("No emails found in input")
