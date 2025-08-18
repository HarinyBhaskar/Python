# Word Frequency Counter using Dict & Set

def word_frequency(filename):
    freq = {}           # dict → word : count
    unique_words = set()  # set → all unique words
    
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            words = line.strip().lower().split()
            for word in words:
                # remove punctuation
                word = ''.join(ch for ch in word if ch.isalnum())
                if word:
                    freq[word] = freq.get(word, 0) + 1
                    unique_words.add(word)   # track unique words

    # Sort by frequency (highest first)
    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    print("\nTop 10 most common words:")
    for word, count in sorted_words[:10]:
        print(f"{word}: {count}")

    print("\nTotal unique words:", len(unique_words))
    print("Some unique words:", list(unique_words)[:10])

# --- Run ---
filename = "sample.txt"  # replace with your file name
word_frequency(filename)
