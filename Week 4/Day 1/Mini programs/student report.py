import logging
from collections import Counter
from itertools import groupby

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    # User enters student records
    n = int(input("Enter number of students: "))
    students = []
    for i in range(n):
        name = input(f"Student {i+1} name: ")
        grade = input("Enter grade (A/B/C...): ")
        students.append((name, grade))

    # Grade distribution
    grade_count = Counter([s[1] for s in students])
    logging.info(f"Grade distribution: {dict(grade_count)}")
    print(f"\nGrade Distribution: {dict(grade_count)}")

    # Group students by grade
    students.sort(key=lambda x: x[1])
    grouped = {k: [s[0] for s in g] for k, g in groupby(students, key=lambda x: x[1])}
    logging.info(f"Grouped students: {grouped}")
    print(f"\nStudents grouped by grade: {grouped}")

if __name__ == "__main__":
    main()
