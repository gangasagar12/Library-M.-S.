class User:
    def __init__(self,username, password,role="user"):
        self.usernaname=username
        self.password=password
        self.role=role

# Class to manage library operations
class Library:
    def __init__(self):
        self.books = []  # List to store available books
        self.borrowed_books = {}  # Dictionary to store borrowed books with username

    def add_book(self,title, author, isbn,year):
        book = {
            "tittle": title,
           "author": author,
           "isbn":isbn,
           "year": year 
        }
        self.books.append(book)
        # self.books.append(title)
        # self.books.append(author)
        print(f"{book} added to the library.")

    def remove_book(self, book):
        for book in self.books:
            if book["isbn"]==isbn:
                self.books.remove(book)
                print(f"{book} removed from the library.")
                return
            print(f"{book} is not found in the library.")

    def search_book(self, title):
      found=[book for book in self.book if title.lower() in book["title"].lower()]
      if found:
        print(f"{title} is available in the library.")
        for book in found: 
            print("-" ,book)
        else:
            print(f"{title} is not available.")

    def borrow_book(self, isbn, username):
        for  book in self.books:
            if book["isbn"]==isbn:
                self.books.remove(book)
            self.borrowed_books[book] = username
            print(f"{book} borrowed by {username}")
        else:
            print(f"{isbn} is not available for borrowing.")

    def return_book(self, isbn, username):
        if self.borrowed_books.get(book) == username:
            #  find book info 
            # for demo recostrcution book minimally (could be improved)
            title=input("enter the book title to return : ")
            author=input(" enter author to return: ")
            year=input(" enter year to return : ")
            book={
                "title": title,
                "author":author,
                "isbn": isbn,
                "year" : year
            }
        
            self.books.append(book)
            del self.borrowed_books[isbn]
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
        self.users = {
            "admin": User("gangasagar" ," 1234"," admin"),
            "user1":User("user1","pass","user")
        }
    def register(self):
        username=input("choose a username: ")
        if username in self.users:
            print(" username already exits.")
            return None
        password=input("choose a password: ")
        role=input(" role( ' admin or ' user, defult is 'user): ")
        if role not in["admin","user"]:
            role="user"
            self.users[username]=user(username, password, role)
            print(f" user {username} registered sucessfully as { role}.")
            return self.users[username]


# === Main Program Starts Here ===
library = Library()
user_system = UserSystem()
while True:
    print("\n=========== library  system====")
    print("1.login")
    print("2. register")
    print("3. exit ")
    main_choice=input("enter choice(1-3): ")
    if main_choice=="1":
        user=user_system.login()
        if user:
            while True:
                print("\n =========DISPLAY OF MENU OF LIBRARY :")
                print("1. Add book(admin book only)")
                print("2. Remove book(admin only)")
                print("3. Search book")
                print("4. Borrow book")
                print("5. Return book")
                print("6. Show all books")
                print("7 change password.")
                print("logout")
            
                choice = input("Enter choice (1-7): ")
        #  perform operations based on the user choice
                if choice=='1':
                    if user.role!="admin":
                        print(" admin acess required.")
                        continue
                    title=input("enter book  tittle ")
                    author=input("enter book tittle")
                    isbn=input(" enter ISBN: ")
                    year=input(" enter year: ")
                    library.add.book(title,author,isbn,year)
                elif choice=="2":
                    if user.role!="admin":
                        print(" in here admin acess required : ")
                        continue
                    isbn=input(" enter isbn of book to remove")
                    library.remove_book(isbn)
                elif choice=="3":
                    title = input("Enter book title to search: ")
                    library.search_book(title)
                elif choice == "4":
                    isbn = input("Enter ISBN of book to borrow: ")
                    library.borrow_book(isbn, user.username)
                elif choice == "5":
                    isbn = input("Enter ISBN of book to return: ")
                    library.return_book(isbn, user.username)
                elif choice == "6":
                    library.show_books()
                elif choice == "7":
                    user_system.change_password(user)
                elif choice == "8":
                    print("Logging out...")
                    break
                else:
                    print("Invalid choice! Please try again.")
    elif main_choice == "2":
        user_system.register()
    elif main_choice == "3":
        print("Thank you for using the library management system!")
        break
    else:
        print("Invalid choice! Please try again.")

