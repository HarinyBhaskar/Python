# validator.py
import logging, re
logging.basicConfig(filename="validator.log", level=logging.INFO)

class URLValidator:
    def __init__(self):
        self.pattern = re.compile(r"^https?://[a-zA-Z0-9.-]+(?:/[^\s]*)?$")

    def is_valid(self, url):
        ok = self.pattern.match(url) is not None
        if ok:
            logging.info("Valid URL: %s", url)
        else:
            logging.warning("Invalid URL: %s", url)
        return ok

if __name__ == "__main__":
    v = URLValidator()
    url = input("Enter a URL: ")
    print("Valid?", v.is_valid(url))
