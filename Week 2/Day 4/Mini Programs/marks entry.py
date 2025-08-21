import logging

logging.basicConfig(filename="marks.log", level=logging.ERROR)

marks = {}

try:
    name = input("Enter student name: ")
    score = int(input("Enter marks (0-100): "))
    if not 0 <= score <= 100:
        raise ValueError("Marks must be between 0 and 100")
    marks[name] = score
    print("Marks saved:", marks)
except ValueError as e:
    logging.error(e)
    print("Error:", e)
