import fetchProcedures


def borrower_question_one(self):
    self.id = input("Enter your card number.\n")
    # Valid card number check here boolean
    result=fetchProcedures.validateCardNo(self.id)
    print(result)
    card = None
    if result is None:
        print("Not a valid ID")
        self.error = "Not valid Id"
    else:
        card=True
    if card == True:
        self.choice = input("1) Check out a book\n2) Return a book\n")
    else:
        pass

def admin_question_one(self):
    self.choice = input("1) Add/Update/Delete Book and Author\n2) Add/Update/Delete Publishers\n3) Add/Update/Delete Library Branches\n4) Add/Update/Delete Borrowers\n5) Over-ride Due Date for a Book Loan\n6)Exit \n")
    

    
    