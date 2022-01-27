# List of book
# Displaying Book
# Adding Book
# Lending Book





class Library:
    def __init__(self,bookList):
        self.List_of_Book=bookList
        self.UserList=[]
        self.LendBookList=[]
        
    @property
    def ViewBooks(self):
        for i in range(len(self.List_of_Book)):
            print(f"{i+1}-{self.List_of_Book[i]}")
    
    def AddBook(self,Book):
        try:
            self.List_of_Book.append(Book)
        
        except Exception as e:
            print(e)

    def BookSearch(self,Book):
        if Book in self.List_of_Book:
            print("Yes Book is Available")
            return 1
        else:
            print("Sorry for inconvenience")        
            return 0

    def BorrowBook(self,book):
        if book in self.List_of_Book:
            print("Enter your name:-",end=' ')
            UserName=input()
            print("Enter your Address:-",end=' ')
            UserAddress=input()
            print("Enter your Phone No.:-",end=' ')
            UserPhone=int(input())
            self.UserList.append({"Name":UserName,"Address":UserAddress,"Phone":UserPhone,"Book":book})
            self.LendBookList.append(book)
   
    @property
    def ViewUserList(self):
        for i in range(len(self.UserList)):
            print(f"{i+1}:{self.UserList[i]}")


if __name__=='__main__':
    
    bookList=["Harry Potter" ,"Rich Dad Poor Dad"]   
    NeelLibrarySanstan=Library(bookList)

    while 1:
        print("1:Librarian")
        print("2:User")
        
        BaseInput=int(input())

        if BaseInput==1:
            print("Please! select an operation")
            print("1:View List of Books")
            print("2:Add New Book")
            print("3:View Borrower List")
            
            LibrarianInput=int(input(
            ))
             
            if LibrarianInput==1:
                NeelLibrarySanstan.ViewBooks
            elif LibrarianInput==2:
                print("Please Enter Book Name:-",end=' ')
                NewBook=input()
                NeelLibrarySanstan.AddBook(NewBook)
            elif LibrarianInput==3:
                NeelLibrarySanstan.ViewUserList
            else:
                print("Please! give a valid input.")
        
        elif BaseInput==2:
            print("Please! select an operation")
            print("1:View List of Books")
            print("2:Borrower Book")
            
            UserInput=int(input())
             
            if UserInput==1:
                NeelLibrarySanstan.ViewBooks
            elif UserInput==2:
                print("Enter the name of Book:-",end=' ')
                BookName=input()
                if(NeelLibrarySanstan.BookSearch(BookName)):
                    NeelLibrarySanstan.BorrowBook(BookName)

            else:
                print("Please! enter a valid input..")        





        

