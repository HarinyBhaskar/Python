from collections import Counter
import re

def count_words(feedback_list):
    """Counts word frequency in a list of feedback strings"""
    words = []
    for feedback in feedback_list:
        feedback = re.sub(r'[^a-zA-Z\s]', '', feedback).lower()  # clean text
        words.extend(feedback.split())
    return Counter(words)
