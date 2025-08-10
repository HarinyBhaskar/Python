name = input("Enter your name: ")
marks = float(input("Enter your marks (0-100): "))

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 50:
    grade = "C"
else:
    grade = "F"

print("\n--- Grade Report ---")
print("Name:", name)
print("Marks:", marks)
print("Grade:", grade)
