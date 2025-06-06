# Class to manage library operations
class Library:
    def __init__(self):
        self.books = []  # List to store available books
        self.borrowed_books = {}  # Dictionary to store borrowed books with username

    def add_book(self, book):
        self.books.append(book)
        print(f"{book} added to the library.")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"{book} removed from the library.")
        else:
            print(f"{book} is not found in the library.")

    def search_book(self, title):
        if title in self.books:
            print(f"{title} is available in the library.")
        else:
            print(f"{title} is not available.")

    def borrow_book(self, book, username):
        if book in self.books:
            self.books.remove(book)
            self.borrowed_books[book] = username
            print(f"{book} borrowed by {username}")
        else:
            print(f"{book} is not available for borrowing.")

    def return_book(self, book, username):
        if self.borrowed_books.get(book) == username:
            self.books.append(book)
            del self.borrowed_books[book]
            print(f"{book} returned by {username}.")
        else:
            print(f"{username} did not borrow {book}.")

    def show_books(self):
        print(f"\nAvailable books ({len(self.books)}):")
        for book in self.books:
            print("-", book)


# Class to manage user login system
class UserSystem:
    def __init__(self):
        self.users = {"gangasagar": "1234", "user1": "pass"}

    def login(self, username, password):
        if self.users.get(username) == password:
            print(f"Welcome, {username}")
            return True
        else:
            print("Invalid username or password.")
            return False


# === Main Program Starts Here ===
library = Library()
user_system = UserSystem()

username = input("Enter username: ")
password = input("Enter password: ")

if user_system.login(username, password):
    while True:
        print("\n =========DISPLAY OF MENU OF LIBRARY :")
        print("1. Add book")
        print("2. Remove book")
        print("3. Search book")
        print("4. Borrow book")
        print("5. Return book")
        print("6. Show all books")
        print("7. Exit")

        choice = input("Enter choice (1-7): ")

        