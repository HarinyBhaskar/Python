import csv, datetime, os

base_path = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(base_path, "patients.csv")
log_file = os.path.join(base_path, "hospital_log.txt")

# Ensure CSV has headings
if not os.path.exists(csv_file):
    with open(csv_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["PatientID", "Name", "Age", "Disease", "AdmissionDate"])

# Add patient
pid = input("Enter Patient ID: ")
name = input("Enter Patient Name: ")
age = input("Enter Age: ")
disease = input("Enter Disease: ")

with open(csv_file, "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([pid, name, age, disease, datetime.datetime.now().strftime("%Y-%m-%d")])

# Log action
with open(log_file, "a") as f:
    f.write(f"{datetime.datetime.now()} - Admitted {name} ({pid}), Disease: {disease}\n")

print(" Patient data saved in patients.csv and logged in hospital_log.txt")
