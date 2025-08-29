# library.py
import logging
logging.basicConfig(filename="library.log", level=logging.INFO)

class Library:
    def __init__(self):
        self.books = []
        logging.info("Library created")

    def add_book(self, title):
        if not title.strip():
            logging.error("Empty title")
            raise ValueError("Book title cannot be empty")
        self.books.append(title.strip())
        logging.info("Book added: %s", title)

    def has_book(self, title):
        found = title.strip() in self.books
        logging.info("Check book '%s' -> %s", title, found)
        return found

    def remove_book(self, title):
        if title in self.books:
            self.books.remove(title)
            logging.info("Removed: %s", title)
            return True
        logging.warning("Book not found: %s", title)
        return False

if __name__ == "__main__":
    lib = Library()
    for b in input("Enter books (comma-separated): ").split(","):
        lib.add_book(b)
    query = input("Search book: ")
    print("Found?", lib.has_book(query))
