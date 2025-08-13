students = ["Hari", "sita", "Charlie", "David", "Eva"]
attendance = {}

print(" Daily Attendance Tracker ")
for student in students:
    status = input(f"Is {student} present? (y/n): ").lower()
    if status not in ["y", "n"]:
        print("Invalid input. Marked absent by default.")
        attendance[student] = "Absent"
        continue
    attendance[student] = "Present" if status == "y" else "Absent"

print("\n Attendance Report ")
present_count = 0
for name, status in attendance.items():
    print(f"{name}: {status}")
    if status == "Present":
        present_count += 1
else:
    print(f"Total Present: {present_count}/{len(students)}")
