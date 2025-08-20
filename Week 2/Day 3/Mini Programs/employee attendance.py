import csv, datetime, os

# File paths
base_path = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(base_path, "attendance.csv")
log_file = os.path.join(base_path, "attendance_log.txt")

# Ensure CSV has headings
if not os.path.exists(csv_file):
    with open(csv_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["EmployeeID", "Name", "Status", "DateTime"])

# Take input
emp_id = input("Enter Employee ID: ")
name = input("Enter Employee Name: ")
status = input("Enter status (Present/Absent): ")

# Save in CSV
with open(csv_file, "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([emp_id, name, status, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")])

# Log in TXT
with open(log_file, "a") as f:
    f.write(f"{datetime.datetime.now()} - {name} ({emp_id}) marked as {status}\n")

print("Attendance recorded in attendance.csv and logged in attendance_log.txt")
