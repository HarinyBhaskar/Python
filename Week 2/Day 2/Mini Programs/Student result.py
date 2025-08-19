def calculate_result(student_name, *marks, **options):
    
    print(f"\nResult for {student_name}")
    print("-" * 40)

    total = sum(marks)  # *args stores marks in tuple
    avg = total / len(marks)

    pass_mark = options.get("pass_mark", 35)
    bonus = options.get("bonus", 0)

    avg += bonus  # add bonus marks

    status = "Pass" if all(m >= pass_mark for m in marks) else "Fail"

    print(f"Marks Entered : {marks}")
    print(f"Total Marks   : {total}")
    print(f"Average       : {avg:.2f}")
    print(f"Result        : {status}")
    print("-" * 40)


calculate_result(
    "Suresh",
    78, 85, 92, 60,
    bonus=2
)

calculate_result(
    "Neha",
    40, 25, 55,
    pass_mark=40
)
