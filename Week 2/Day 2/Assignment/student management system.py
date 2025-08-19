# --- Custom map & filter ---
def my_map(func, iterable):
    return [func(item) for item in iterable]

def my_filter(func, iterable):
    return [item for item in iterable if func(item)]


# --- Student Registration ---
def add_student(name, *subjects, **details):
    return {
        "name": name,
        "subjects": subjects,       # variable subjects
        "details": details          # flexible info like marks, year, hostel
    }


# --- Student Records ---
students = [
    add_student("Arjun", "Math", "Physics", marks=85, year=2, hostel=True),
    add_student("Neha", "Chemistry", "Biology", marks=92, year=1),
    add_student("Vikram", "History", "Economics", marks=70, year=3, hostel=True),
    add_student("Riya", "Math", "CS", marks=95, year=2),
]

# --- Use custom map & filter ---
high_scorers = my_filter(lambda s: s["details"]["marks"] > 80, students)
names = my_map(lambda s: s["name"], high_scorers)

print("High Scoring Students:", names)
print("Hostel Students:", [s["name"] for s in students if s["details"].get("hostel")])
