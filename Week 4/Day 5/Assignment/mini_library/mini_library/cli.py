import argparse
from mini_library import library

def main():
    parser = argparse.ArgumentParser(description="Mini Library CLI")
    subparsers = parser.add_subparsers(dest="command")

    # add book
    parser_add = subparsers.add_parser("add", help="Add a new book")
    parser_add.add_argument("title", type=str, help="Book title")
    parser_add.add_argument("author", type=str, help="Book author")

    # list books
    subparsers.add_parser("list", help="List all books")

    # search books
    parser_search = subparsers.add_parser("search", help="Search for a book by keyword")
    parser_search.add_argument("keyword", type=str, help="Keyword to search")

    args = parser.parse_args()

    if args.command == "add":
        print(library.add_book(args.title, args.author))
    elif args.command == "list":
        print(library.list_books())
    elif args.command == "search":
        print(library.search_book(args.keyword))
    else:
        parser.print_help()
