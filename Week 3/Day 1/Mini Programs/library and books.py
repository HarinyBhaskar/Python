class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added: {book}")

    def show_books(self):
        if not self.books:
            print("Library is empty")
        else:
            print("Books in Library:")
            for book in self.books:
                print("-", book)

# Example usage
b1 = Book("Python Crash Course", "Eric Matthes")
b2 = Book("Clean Code", "Robert C. Martin")

lib = Library()
lib.add_book(b1)
lib.add_book(b2)
lib.show_books()
