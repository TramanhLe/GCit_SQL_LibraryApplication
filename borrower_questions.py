<<<<<<< HEAD
import fetchProcedures
=======


>>>>>>> 2f9bebd1bd75740e5946311647a53f2deefe2dd4

def question_one(self):
    self.id = input("Enter your card number.\n")
    # Valid card number check here boolean -check-
    result=fetchProcedures.validateCardNo(self.id)
    card = None
    if len(result)==0:
        print("Not a valid ID")
    else:
        card=True
    
    if card == True:
        self.choice = input("1) Check out a book\n 2) Return a book\n")
        self.next()
    else:
        pass

<<<<<<< HEAD
=======

>>>>>>> 2f9bebd1bd75740e5946311647a53f2deefe2dd4

def question_two(self):
    if self.choice == "1":
        # Get library branches here -check-
        branches=fetchProcedures.fetchBranchs()
        for x in branches:
            print(x)
        branchInput = input(" Which branch do you want to check out from?")
        #using which branchInput to grab list of books from the proper branch
        self.next()
    elif self.choice == "2": 
<<<<<<< HEAD
        # Get books this borrower has checked out -check-
        books=fetchProcedures.fetchBorrowerBooks(self.id)
        for x in branches:
            print(x)
        self.next()
=======
        # Get books this borrower has checked out
        books = ["Romeo","Juliet","Ron Howard"]
        self.next()


def question_three(self):
    print("Hello from question 3")
    self.next()
>>>>>>> 2f9bebd1bd75740e5946311647a53f2deefe2dd4
