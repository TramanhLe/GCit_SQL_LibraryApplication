import string_utils
import updateProcedures
import fetchProcedures

def start(self):
    self.store["cardNo"] = input("Enter the borrower Card Number you want to update the due date for?\n")
    books = fetchProcedures.fetchBooksByBorrowerId()
    books = string_utils.build_input_options(self, books)
    self.choice = input("Which book do you want to update the due date for?\n" + books)
    self.store["bookId"] = self.grab()