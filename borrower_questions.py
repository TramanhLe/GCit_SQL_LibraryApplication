import fetchProcedures

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
        # Get books this borrower has checked out -check-
        books=fetchProcedures.fetchBorrowerBooks(self.id)
        for x in branches:
            print(x)
        self.next()
