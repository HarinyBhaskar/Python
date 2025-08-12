
name = input("Enter your name: ")
math_marks = int(input("Enter marks in Mathematics (out of 100): "))
science_marks = int(input("Enter marks in Science (out of 100): "))
english_marks = int(input("Enter marks in English (out of 100): "))
entrance_score = int(input("Enter Entrance Exam score (out of 100): "))
category = input("Enter your category (General/SC/ST/OBC): ").strip().lower()

if math_marks >= 60 and science_marks >= 55 and english_marks >= 50 and entrance_score >= 60:
    if category in ["sc", "st", "obc"]:
        print(f"Congratulations {name}! You are eligible for admission with reservation benefits.")
    else:
        print(f"Congratulations {name}! You are eligible for admission in the General category.")
else:
    print(f"Sorry {name}, you do not meet the eligibility criteria.")
    print("Minimum requirements: Maths >= 60, Science >= 55, English >= 50, Entrance >= 60.")

print("Thank you for applying!")
