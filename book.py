# Initial commit: Define custom exceptions and Book class
class BookNotAvailableError(Exception):
    """Raised when a book is requested for borrowing but is already borrowed."""
    pass

class BookNotFoundError(Exception):
    """Raised when a book with a given ISBN is not found in the library."""
    pass

class Book:
    def __init__(self, isbn: str, title: str, author: str, publication_year: int):
        # Initialize the book with its details and a flag for availability
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_borrowed = False  # Book is initially available

    def __str__(self):
        # Return a string representation of the book for easy printing
        return f"{self.title} by {self.author} (ISBN: {self.isbn}, Year: {self.publication_year})"

# Commit message: "Add custom exceptions and Book class"
# git add library_management.py
# git commit -m "Add custom exceptions and Book class"

# Implement Library class with basic functionalities: add_book, borrow_book, return_book, and view_available_books
class Library:
    def __init__(self):
        # Initialize the library with an empty dictionary to store books by ISBN
        self.books = {}

    def add_book(self, book: Book):
        """
        Add a new book to the library.
        If the book already exists (based on ISBN), raise a ValueError.
        """
        if book.isbn in self.books:
            raise ValueError(f"Book with ISBN {book.isbn} already exists.")
        self.books[book.isbn] = book
        print(f"Book '{book.title}' added to the library.")

    def borrow_book(self, isbn: str) -> Book:
        """
        Borrow a book from the library.
        Raise BookNotFoundError if the book doesn't exist.
        Raise BookNotAvailableError if the book is already borrowed.
        """
        if isbn not in self.books:
            raise BookNotFoundError(f"Book with ISBN {isbn} not found.")
        book = self.books[isbn]
        if book.is_borrowed:
            raise BookNotAvailableError(f"The book '{book.title}' is currently borrowed.")
        book.is_borrowed = True  # Mark the book as borrowed
        print(f"Book '{book.title}' has been borrowed.")
        return book

    def return_book(self, isbn: str):
        """
        Return a borrowed book to the library.
        Raise BookNotFoundError if the book doesn't exist.
        """
        if isbn not in self.books:
            raise BookNotFoundError(f"Book with ISBN {isbn} not found.")
        book = self.books[isbn]
        if not book.is_borrowed:
            print(f"The book '{book.title}' was not borrowed.")
        else:
            book.is_borrowed = False  # Mark the book as returned
            print(f"Book '{book.title}' has been returned.")

    def view_available_books(self):
        """
        Print all available (not borrowed) books in the library.
        If no books are available, print a message indicating so.
        """
        available_books = [book for book in self.books.values() if not book.is_borrowed]
        if available_books:
            print("Available books:")
            for book in available_books:
                print(f"  - {book}")
        else:
            print("No books are currently available.")

# Commit message: "Implement Library class with add, borrow, return, and view functions"
# git add library_management.py
# git commit -m "Implement Library class with add, borrow, return, and view functions"

# Add a sample usage block for demonstration
if __name__ == "__main__":
    library = Library()

    # Adding books to the library
    library.add_book(Book("12345", "Python Programming", "John Doe", 2020))
    library.add_book(Book("67890", "Data Science with Python", "Jane Doe", 2021))

    # Viewing available books
    library.view_available_books()

    # Borrowing a book
    try:
        library.borrow_book("12345")
    except BookNotAvailableError as e:
        print(e)
    except BookNotFoundError as e:
        print(e)

    # Trying to borrow the same book again
    try:
        library.borrow_book("12345")
    except BookNotAvailableError as e:
        print(e)
    except BookNotFoundError as e:
        print(e)

    # Returning a book
    try:
        library.return_book("12345")
    except BookNotFoundError as e:
        print(e)

    # Viewing available books after returning one
    library.view_available_books()

    # Trying to borrow a non-existent book
    try:
        library.borrow_book("00000")
    except BookNotAvailableError as e:
        print(e)
    except BookNotFoundError as e:
        print(e)

# Commit message: "Add sample usage with error handling demonstration"
# git add library_management.py
# git commit -m "Add sample usage with error handling demonstration"
