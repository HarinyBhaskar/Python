# Hospital Patient Management

patients = [
    ("John Doe", 45, "Flu"),
    ("Jane Smith", 30, "Fracture")
]

def admit_patient(name, age, illness):
    patients.append((name, age, illness))
    print(f"Admitted patient: {name}")

def display_patients():
    print("\nPatient Records:")
    for name, age, illness in patients:
        print(f"{name}, {age} years - {illness}")

display_patients()
admit_patient("Alice Brown", 55, "Pneumonia")
display_patients()
