import logging

logging.basicConfig(filename="library.log", level=logging.INFO)

books = {"Python Basics": True, "AI Intro": False}

try:
    book = input("Enter book to issue: ")
    if book not in books:
        raise KeyError("Book not in library")
    if not books[book]:
        raise ValueError("Book already issued")
    books[book] = False
    logging.info(f"Issued: {book}")
    print(f"Book '{book}' issued successfully.")
except (KeyError, ValueError) as e:
    logging.error(e)
    print("Error:", e)
