students = {
    "Alice": ["Math", "Python"],
    "Bob": ["Science"]
}

# Set of all offered courses
courses = {"Math", "Science", "Python", "AI"}

def register_course(student, course):
    if course in courses:
        students.setdefault(student, []).append(course)
        print(f"{student} registered for {course}.")
    else:
        print("Course not offered.")

def show_students():
    print("\nStudent Registrations:")
    for name, course_list in students.items():
        print(f"{name}: {course_list}")

def show_courses():
    print("\nAll Offered Courses:", courses)


register_course("Charlie", "AI")
register_course("Alice", "Science")
show_students()
show_courses()
