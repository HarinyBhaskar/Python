from Utils import parse_feedback_csv, count_words

# Read feedback data from CSV
feedback_data = parse_feedback_csv("feedback.csv")
print("Customer Feedback:", feedback_data)

# Count word frequency
word_freq = count_words(feedback_data)
print("\nTop 5 Most Common Words in Feedback:")
for word, freq in word_freq.most_common(5):
    print(f"{word}: {freq}")
