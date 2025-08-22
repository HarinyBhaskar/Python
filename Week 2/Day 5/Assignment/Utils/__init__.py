import csv
from collections import Counter
import re
from .csv_parser import parse_feedback_csv
from .word_counter import count_words

def parse_feedback_csv(file_path):
    feedback_list = []
    with open(file_path, newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            feedback_list.append(row["feedback"])
    return feedback_list

def count_words(feedback_list):
    words = []
    for feedback in feedback_list:
        feedback = re.sub(r'[^a-zA-Z\s]', '', feedback).lower()
        words.extend(feedback.split())
    return Counter(words)
