import string_utils
import fetchProcedures



def question_two(self):
    if self.choice == "1":
        # Get library branches here
        branches=fetchProcedures.fetchBranchs()
        branches = string_utils.build_input_options(branches)
        branch = input("Which branch do you want to check out from?\n" + branches)
        self.choice = branch
        self.next()
    elif self.choice == "2": 
        # Get books this borrower has checked out
        books=fetchProcedures.fetchBorrowerBooks(self.id)
        books = string_utils.build_input_options(books)
        self.next()


def question_three(self):
    books = ["book1","book2", "book3"]
    books = string_utils.build_input_options(books)
    input("Which book would you like to check out?\n" + books)
    self.next()
    

def return_to_initial_question(self):    
    self.home()

