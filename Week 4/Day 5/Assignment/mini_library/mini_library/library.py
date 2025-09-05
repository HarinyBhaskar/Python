books = []

def add_book(title, author):
    books.append({"title": title, "author": author})
    return f"Book added: {title} by {author}"

def list_books():
    if not books:
        return "No books in the library!"
    return "\n".join([f"{i+1}. {b['title']} by {b['author']}" for i, b in enumerate(books)])

def search_book(keyword):
    results = [f"{b['title']} by {b['author']}" for b in books if keyword.lower() in b['title'].lower()]
    return "\n".join(results) if results else "No matching books found."
