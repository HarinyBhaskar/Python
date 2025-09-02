import re, logging
from collections import Counter

logging.basicConfig(filename="words.log", level=logging.INFO)

def word_count(text):
    words = re.findall(r"\b\w+\b", text.lower())
    return Counter(words)

if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    counts = word_count(sentence)
    print("📊 Word frequency:")
    for word, count in counts.items():
        print(f"{word}: {count}")
    logging.info(f"Word counts: {counts}")
