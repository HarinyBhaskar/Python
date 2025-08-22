import csv

def parse_feedback_csv(file_path):
    """Reads a CSV file and extracts feedback column"""
    feedback_list = []
    with open(file_path, newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            feedback_list.append(row["feedback"])  # 'feedback' column must exist
    return feedback_list
