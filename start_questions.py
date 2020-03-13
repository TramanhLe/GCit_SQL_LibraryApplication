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

def lib_question_start(self):
    self.choice = input("1)Enter Branch you manage\n 2)Quit to previous\n" )
    
