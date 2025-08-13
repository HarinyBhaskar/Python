books = ["Python Basics", "Data Science 101", "AI for Beginners", "Web Dev with Flask"]
borrowed_books = []

print(" Welcome to the Library ")
while True:
    print("\nAvailable books:")
    for b in books:
        print(f"- {b}")

    choice = input("\nEnter book name to borrow (or 'exit'): ").title()
    if choice.lower() == "exit":
        break
    if choice not in books:
        print("Sorry, that book is not available.")
        continue

    books.remove(choice)
    borrowed_books.append(choice)
    print(f"You borrowed '{choice}'.")

print("\n Borrow Summary ")
if borrowed_books:
    for book in borrowed_books:
        print(f"- {book}")
else:
    print("No books borrowed.")
print("Thank you for visiting!")
