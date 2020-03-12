def question_one(self):
    self.id = input("Enter your card number.\n")
    # Valid card number check here boolean
    card = True
    if card == True:
        self.choice = input("1) Check out a book\n 2) Return a book\n")
        self.next()
    else:
        pass


def question_two(self):
    if self.choice == "1":
        # Get library branches here
        branches = ["New York", "New Mexico", "New Hampshire", "New Zealand"]
        for i, count in enumerate(branches):
            print(count)
        branch = input(""" Which branch do you want 
                          to check out from?\n 1) {branches[0]}\n
                           2) {branches[1]}\n
                            3) {branches[2]}""")
        self.next()
    elif self.choice == "2": 
        # Get books this borrower has checked out
        books = ["Romeo","Juliet","Ron Howard"]
        self.next()