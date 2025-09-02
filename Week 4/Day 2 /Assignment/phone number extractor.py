import re
import logging

# Setup logging
logging.basicConfig(
    filename="extractor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def extract_contacts(text):
    # Regex for emails
    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}", text)
    # Regex for phone numbers (international + local formats)
    phones = re.findall(r"\+?\d{1,3}?[-.\s]?\(?\d{2,4}\)?[-.\s]?\d{3,4}[-.\s]?\d{3,4}", text)
    return emails, phones

if __name__ == "__main__":
    raw_text = input("Enter raw text containing emails & phone numbers:\n")
    emails, phones = extract_contacts(raw_text)

    print("\n📧 Emails found:")
    print(emails if emails else "None")
    print("\n📱 Phone numbers found:")
    print(phones if phones else "None")

    logging.info(f"Extracted emails: {emails}")
    logging.info(f"Extracted phones: {phones}")
