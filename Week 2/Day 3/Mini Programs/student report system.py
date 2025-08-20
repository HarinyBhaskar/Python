import os, csv, datetime

# Save inside the same folder as the Python file
base_path = os.path.dirname(os.path.abspath(__file__))

students_file = os.path.join(base_path, "students.csv")
log_file = os.path.join(base_path, "report_log.txt")

# Add student details to CSV file
with open(students_file, "a", newline="") as f:
    writer = csv.writer(f)
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    grade = "A" if marks >= 90 else "B" if marks >= 75 else "C"
    writer.writerow([name, marks, grade])

# Log the action in text file
with open(log_file, "a") as f:
    f.write(f"{datetime.datetime.now()} - Added {name} with marks {marks} and grade {grade}\n")

print(" Data saved in students.csv and log created in report_log.txt")
