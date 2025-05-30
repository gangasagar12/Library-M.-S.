
# === Main Program Starts Here ===

# Create instances of Library and UserSystem
library = Library()
user_system = UserSystem()

# Get user credentials
username = input("Enter username: ")
password = input("Enter password: ")

# If login successful, show menu options
if user_system.login(username, password):
    while True:
        # Display the menu
        print("\nMenu:")
        print("1. Add book")
        print("2. Remove book")
        print("3. Search book")
        print("4. Borrow book")
        print("5. Return book")
        print("6. Show all books")
        print("7. Exit")
