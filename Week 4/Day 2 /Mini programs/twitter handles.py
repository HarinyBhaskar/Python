import re, logging

logging.basicConfig(filename="handles.log", level=logging.INFO)

def extract_handles(text):
    return re.findall(r"@\w+", text)

if __name__ == "__main__":
    tweet = input("Enter a tweet: ")
    handles = extract_handles(tweet)
    print("📢 Handles found:", handles)
    logging.info(f"Handles: {handles}")
