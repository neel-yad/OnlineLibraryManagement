# List of book
# Displaying Book
# Adding Book
# Lending Book
from os import remove
from django.forms import PasswordInput


class Library:
    def __init__(self, bookList):
        self.List_of_Book = bookList
        self.UserList = []
        self.LendBookList = []

    @property
    def ViewBooks(self):
        for i in range(len(self.List_of_Book)):
            print(f"{i+1}-{self.List_of_Book[i]}")
        print()

    def AddBook(self, Book):
        try:
            self.List_of_Book.append(Book)

        except Exception as e:
            print(e)

    def BookSearch(self, Book):
        if Book in self.List_of_Book:
            print("Yes Book is Available \n")
            return 1
        else:
            print("Sorry Book is not available \n")
            return 0

    def BorrowBook(self, book):
        if book in self.List_of_Book:
            print("Yes Book is Available \n")
            print("Enter your name:-", end=' ')
            UserName = input()
            print("Enter your Address:-", end=' ')
            UserAddress = input()
            print("Enter your Phone No.:-", end=' ')
            UserPhone = int(input())
            print()
            self.List_of_Book.remove(book)
            self.UserList.append(
                {"Name": UserName, "Address": UserAddress, "Phone": UserPhone, "Book": book})
            self.LendBookList.append(book)
        
        else:
            for i in range(len(self.UserList)):
                if(self.UserList[i]['Book']==book):
                    print("Currently this book had been borrowed by:-")
                    print(f"\nName:-{self.UserList[i]['Name']} \n Address:-{self.UserList[i]['Address']} \n Phone:-{self.UserList[i]['Phone']} \n")
                    break
                print("Sorry for this book is not available..")
    
    def ReturnBook(self,book,name,phoneNumer):
        self.List_of_Book.append(book)
        self.LendBookList.remove(book)
        for i in range(len(self.UserList)):
            if self.UserList[i]['Book']==book and self.UserList[i]['Phone']==phoneNumer and self.UserList[i]['Name']==name:
                self.UserList.pop(i)
                break

    @property
    def ViewUserList(self):
        for i in range(len(self.UserList)):
            print(f"{i+1}:-\n Book:-{self.UserList[i]['Book']} \n Name:-{self.UserList[i]['Name']} \n Address:-{self.UserList[i]['Address']} \n Phone:-{self.UserList[i]['Phone']} \n")


def Libranian(NeelLibrarySanstan):
    print(" \n Please! select an operation")
    print("1:View List of Books")
    print("2:Add New Book")
    print("3:View Borrower List \n")
    print("Enter your choice:-",end=' ')


    LibrarianInput = int(input())

    if LibrarianInput == 1:
        NeelLibrarySanstan.ViewBooks
    elif LibrarianInput == 2:
        print("Please Enter Book Name:-", end=' ')
        NewBook = input()
        NeelLibrarySanstan.AddBook(NewBook)
    elif LibrarianInput == 3:
        NeelLibrarySanstan.ViewUserList
    else:
        print("Please! give a valid input.")


def UserLogin(NeelLibrarySanstan):
    print("Please! select an operation")
    print("1:View List of Books")
    print("2:Borrower Book")
    print("3:Return Book \n")
    print("Enter your choice:-",end=' ')
    UserInput = int(input())
    print()
    if UserInput == 1:
        NeelLibrarySanstan.ViewBooks
    elif UserInput == 2:
        print("Enter the name of Book:-", end=' ')
        BookName = input()
        print()
        NeelLibrarySanstan.BorrowBook(BookName)
    elif UserInput==3:
        print("Enter book name:-",end=' ')
        rBookName=input()
        print("Enter your name:-",end=' ')
        u_name=input()
        print("Enter you phone No.")
        phoneNo=int(input())
        NeelLibrarySanstan.ReturnBook(rBookName,u_name,phoneNo)


if __name__ == '__main__':

    bookList = ["Harry Potter", "Rich Dad Poor Dad"]
    NeelLibrarySanstan = Library(bookList)

    while 1:
        print("1:Librarian")
        print("2:User \n")
        print("Enter your choice:-",end='')
        BaseInput = int(input())
        if BaseInput == 1:
            print("Username:-", end=' ')
            Username = input()
            print("Password:-", end=' ')
            Password = input()
            if Username == "neerjyadav21@gmail.com" and Password == "Tanee":
                while 1:
                    Libranian(NeelLibrarySanstan)
                    print("Do you want to logout Y/N",end=':-')
                    Logout=input()
                    print()
                    if Logout=="Y":
                        break 
            else:
                print("Incorrect Username or Password..")

        elif BaseInput == 2:
                
                while 1:
                    UserLogin(NeelLibrarySanstan)
                    print("Do you want to Logout Y/N",end=':-')
                    Logout=input()
                    print()
                    if Logout=="Y":
                        break
        else:
            print("Please! enter a valid input.. \n")
