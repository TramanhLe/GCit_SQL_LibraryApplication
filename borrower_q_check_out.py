import string_utils



def question_two(self):
    if self.choice == "1":
        # Get library branches here
        branches = ["New York", "New Mexico", "New Hampshire", "New Zealand"]
        branches = string_utils.build_input_options(branches)
        branch = input("Which branch do you want to check out from?\n" + branches)
        self.choice = branch
        self.next()
    elif self.choice == "2": 
        # Get books this borrower has checked out
        books = ["Romeo","Juliet","Ron Howard"]
        books = string_utils.build_input_options(books)
        self.next()


def question_three(self):
    print("Hello from question 3")
    self.next()




string_utils.build_input_options(["New York", "New Mexico", "New Hampshire", "New Zealand"])