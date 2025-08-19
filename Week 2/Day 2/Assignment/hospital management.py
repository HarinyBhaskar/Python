# --- Custom map & filter ---
def my_map(func, iterable):
    return [func(item) for item in iterable]

def my_filter(func, iterable):
    return [item for item in iterable if func(item)]


# --- Patient Registration ---
def add_patient(name, *symptoms, **details):
    return {
        "name": name,
        "symptoms": symptoms,        # variable symptoms
        "details": details           # flexible info: age, city, admitted, bill
    }


# --- Patient Records ---
patients = [
    add_patient("Amit", "Fever", "Cough", age=45, city="Delhi", bill=5000, admitted=True),
    add_patient("Sonal", "Headache", age=30, city="Mumbai", bill=1200),
    add_patient("Raghav", "Injury", "Fracture", age=25, city="Delhi", bill=20000, admitted=True),
    add_patient("Meera", "Cold", "Allergy", age=20, city="Chennai", bill=800),
]

# --- Use custom map & filter ---
delhi_patients = my_filter(lambda p: p["details"]["city"] == "Delhi", patients)
bills = my_map(lambda p: p["details"]["bill"], patients)

print("Delhi Patients:", [p["name"] for p in delhi_patients])
print("All Bills:", bills)
