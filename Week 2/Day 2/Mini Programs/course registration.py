def register_courses(*subjects, **student):
   
    print(f"\nRegistration Details")
    print("-" * 40)

    # Student details from kwargs (dictionary)
    for key, value in student.items():
        print(f"{key.capitalize():<12}: {value}")

    # Subjects from args (tuple)
    print("Subjects Registered:", ", ".join(subjects))
    print("-" * 40)


# Example usage
register_courses(
    "Mathematics", "Physics", "Computer Science",
    name="Karthik", roll_no=102, department="Engineering"
)

register_courses(
    "Economics", "Statistics",
    name="Ananya", roll_no=205, department="Commerce"
)
