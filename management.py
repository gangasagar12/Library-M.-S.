import datetime
# import the  SMTP  for sending email
import smtplib 
import random
import string
#  used to class create plain text email parts
from email.mime.text import MIMEText
# multiparts class used to create email message with multiparts such as text and attachment 
from email.mime.multipart import MIMEMultipart
class User:
    def __init__(self, username, password, role="user", email=None):
        self.username = username
        self.password = password
        self.role = role
        #  track  the how many books the user haas borrowed
        self.borrowed_count=0 
        self.email=email
        self.notifications=[]
        #  to track the fine fo the user
        self.fine=0   
        #  logger class for activity logs
class Logger:
    def __init__(self):
        self.activity_logs=[]

        # to add the method records logs and maake the function for it
    def log_activity(self,username,action):
    
            timestamp=datetime.datetime.now().strftime("%Y-%m -%d %H: %M :%S")
      
            log_entry=f"[{timestamp}] {username}: {action}"
            self.activity_logs.append(log_entry)
#  for the set up email sending function

def  send_email(subject,body,recipient_email):
    sender_email="gangasagar62@gmail.com"
    sender_password="gangasagar0239#"
    message=MIMEMultipart()
    message["From"]=sender_email
    message["To"]=recipient_email
    message["subject"]=subject
    message.attach( MIMEText(body,"plain"))
    # connect to the SMPT server and send the email
    try:
        with smtplib.SMTP_SSL("ganga15bca2024@gmail.com",465) as server:
            server.login(sender_email,sender_password)
            server.sendmail(sender_email,recipient_email,message.as_string())
            print("Email sent successfully!")
    except Exception as e:
        print(f"error sending email: {e}")

# Class to manage library operations
class Library:
    # from email_util import send_email
    def __init__(self):
        self.books = []  # List to store available books
        self.borrowed_books = {}  # Dictionary to store borrowed books with username
        self.Logger=Logger()
        self.reservation={}


    def add_book(self,title, author, isbn,year,username):
        book = {
            "title": title,
           "author": author,
           "isbn":isbn,
           "year": year 
        }
        self.books.append(book)
        # self.books.append(title)
        # self.books.append(author)
        self.Logger.log_activity(username,f"added book: {title}(isbn:{isbn})")
        print(f"{book} added to the library.")

    def remove_book(self, isbn,username):
        #  check if the user is admin or not
        user=user_system.users.get(username)
        if user and user.role=="admin":
            for book in self.books:
                if book["isbn"]==isbn:
                    self.books.remove(book)
                    self.Logger.log_activity(username,f"removed book: {book['title']}(isbn:{isbn})")
                    print(f"{book} removed from the library.")
                    return
        print(f"{book} is not found in the library.")

    def search_book(self, title):
      found=[book for book in self.books if title.lower() in book["title"].lower()]
      if found:
        print(f"{title} is available in the library.")
        for book in found: 
            print("-" ,book)
        else:
            print(f"{title} is not available.")
    
    def borrow_book(self, isbn, username,user_system):
         if isbn not in self.books or self.books[isbn]['checked out']:
            #   book is checked out so reverse it
            if isbn not in self.reservation:
                self.reservation[isbn]=[]
                self.reservation[isbn].append(username)
                print(f"{username} added to reservation list for the book{isbn}")
            else:
                print(f" {username} is already in the reservation queue for{isbn} ")
                return False
                #  not biorrowed but reversed
                # otherwise check out the book
            self.books[isbn]['checkout']=True
            self.books[isbn]['borrower']=username
            print
        #   set the maximum number of 
         max_books_peruser=5
         due_day=14
         user=user_system.users.get(username)
         if not user:
             print("user not found.")
             return
         #  check if the user has reached the maximum number of books allowed
         if user.borrowed_count>=max_books_peruser:
             print(f"{username} has reased the limit of maximum number of book to the per user{max_books_peruser} books.")
             return 
        
         for  book in self.books:
            if book["isbn"]==isbn:
                
                self.books.remove(book)
                due_dates=datetime.date.today()+ datetime.timedelta(days=due_day)
                self.borrowed_books[isbn]={
                    "user": username,
                    "due_date":due_dates,
                    "book": book
                }
                                        #  increament the user borrrowd book count
                user.borrowed_count+=1
                self.logger.log_activity(username,f"borrowed book: {book['title']} (ISBN: {isbn})")
                return
    def return_book(self, isbn, username,user_system):
        borrow_info=self.borrowed_books.get(isbn)
        if borrow_info and borrow_info["user"] == username:
            user=user_system.users.get(username)
            if user:
                #  decrement the count of books after the book return
                user.borrowed_count-=1
        if self.borrowed_books.get(isbn) == username:
            user=user_system.users.get(username)
            if user: 
                #  decrement the count of books after the book return
                user.borrowed_count-=1
            #  find book info 
            # for demo recostrcution book minimally (could be improved)
            due_dates=borrow_info["due_date"]
            today=datetime.date.today()
            overdue_days=(today-due_dates).days
            fine=0
            if overdue_days>0:
                fine_rate=10
                fine =overdue_days*fine_rate
                print(f" book is overdue by {overdue_days} days(s). fine: {fine}")
                #  add fine attributres to user if not present
                if not hasattr(user,"fine"):
                    user.fine=0
                    user.fine+=fine
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
        for entry in self.activity_logs:
            print(entry)

    def remannig_borrow_limit(self,username):
        max_book_peruser=5
        user=user_system.users.get(username)
        if user:
            remanining =max_book_peruser-user.borrowed_count
            print(f" {username} can borrowed {remanining} more books(s).")
            return remanining
        print("user not found.")
        return 0
    def notify_due_date(user_email,book_title,due_date):
        subject="library reminder: book due soon"
        body=f"dear user,\n\n your borrowed book '{book_title}' is due on {due_date}.\n please return it on time to avoid fines.\n\n thank you!"
        send_email(subject, body, user_email)
        


# Class to manage user login system
class UserSystem:
    def __init__(self):
        self.users = {
            "admin": User("gangasagar" ," 1234"," admin",email="admin@example.com"),
            "user1":User("user1","pass","user",email="user1@example.com")

        }
        #  email code ,mapping
        self.reset_codes={}
    def login(self):
        username=input("enter username: ")
        password=input(" enter password:")
        user=self.users.get(username)
        if user and user.password==password:
            print(f" welcome{username}")
            return user
        print("invilid username or password.")
        return None
    
    
    
    def register(self):
        username=input("choose a username: ")
        if username in self.users:
            print(" username already exits.")
            return None
        password=input("choose a password: ")
        role=input(" role( ' admin or ' user, defult is 'user): ")
        if role not in["admin","user"]:
            role="user"
            self.users[username]=User(username, password, role)
            print(f" user {username} registered sucessfully as { role}.")
            return self.users[username]
        #  for the due dates and times inmport determine function

    def change_password(self,user):
        new_password=input("enter new password: ")
        user.password=new_password
        print(f" password changed sucessfully for {user.username}")
    def  list_users(self):
        print("\n Registered users : ")
        for username, user in self.users.items():
            print(f" username: {username}, email: {user.email},role{user.role}")

# === Main Program Starts Here ===
library = Library()
user_system = UserSystem()
while True:
    print("\n=========== library  system====")
    print("1.login")
    print("2. register")
    print("3. exit ")
    print("4. forgot password")
    main_choice=input("enter choice(1-3): ")
    if main_choice=="1":
        user=UserSystem.login()
        if user:
            while True:
                print("\n =========DISPLAY OF MENU OF LIBRARY :")
                print("1. Add book(admin book only)")
                print("2. Remove book(admin only)")
                print("3. Search book")
                print("4. Borrow book")
                print("5. Return book")
                print("6. Show all books")
                print("7.view activity logs.")
                print("8 change password.")
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
                elif choice=="7":
                    user_system.activity
                elif choice == "7":
                    user_system.change_password(user)
                elif choice=="8":
                    library.remannig_borrow_limit(user.username)
                elif choice=="9":
                 isbn=input("enter isbn to renuw: ")
                 library.renew_book(isbn,user.username)
                elif choice=="11":
                    isbn=input("enter ISBN to  view reservations: ")
                    library.show_reservations(isbn)
            
                elif choice == "11":
                    user_system.list_users()
                elif choice=="10":
                    print("Logging out...")
                    break
                else:
                    print("Invalid choice! Please try again.")

    elif main_choice == "2":
        user_system.register()
    elif main_choice=="4":
        user_system.forgot_password()
    elif main_choice == "3":
        print("Thank you for using the library management system!")
        break
    else:
        print("Invalid choice! Please try again.")




#  user profile editing
#  view user borrowing history
#  list of all available books
#  activity logs for admin
#  hash and salt password for security
# View all registered users
# Manage users (activate/deactivate accounts)
# View all logs and system statistics