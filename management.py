#  library management
#  class to manage liberary operations
class library:
    def __init__(self):
        # list to store available books
        self.books=[]
        #  dictoinary to store borrowed books with name
        self.borrowed_books={}
        #  add a book to the library
    def add_book(self,book):
        self.books.append(book)
        print(f"{book} added to the library.")

        #  remove a book in the library
    def remove_book(self,book):
        if book in self.books:
            self.books.remove(book)
            print(f"{book} removed form the library.")
        else:
            
        



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
        
     #  get user choice
        choice=input("enter choice)(1-7):")
     #  perform operations based on user choice
        if choice=="1":
            book=input("enter the book name: ")
            library.add_book(book)
        elif choice=="2":
            book=input("enter book tittle to remove: ")
        library.remove_book(book)
elif choice=="3":
      book=input("enter book tittle to search: ")
      library.search_book(book)
                                            
elif choice=="4":
  book=input("enter book tittle to return: ")
  library.borrow_book(book,username)
    
elif choice== "5":
    book=input("enter book tittle to return: ")
    library.return_book(book,username)

elif choice=="6":
    library.show_books()
elif choice=="7":
 print("thank you for using the our librayr management system: ")
    
    break
else:
     print("invilid choice !plese try again:")


