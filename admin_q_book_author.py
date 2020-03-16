import string_utils
import updateProcedures
import fetchProcedures

def start(self):
    print("What would you like to do?\n")
    self.choice = input("1) Add/Update/Delete Book\n2) Add/Update/Delete Author\n")
    if self.choice == "1":
        self.choice = input("1) Add Book\n2) Update Book\n3) Delete Book\n")
        if self.choice == "1":
            add_book_author(self)
        elif self.choice == "2":
            print("Update an existing book")
        elif self.choice == "3":
            print("Delete an existing book")
    elif self.choice == "2":
        self.choice = input("1) Add Author\n2) Update Author\n3) Delete Author\n")
        if self.choice == "1":
            print("Add Author")
        elif self.choice == "2":
            print("Update an existing Author")
        elif self.choice == "3":
            print("Delete an existing Author")


def add_book_author(self):
    self.store["title"] = input("What is the title of the book you want to add?\n")

    authors = fetchProcedures.fetchAuthors()
    authors = string_utils.build_input_options(self, authors)
    self.choice = input("Who authored this book?\n" + authors)
    self.store["author"] = self.grabId()

    publishers =  fetchProcedures.fetchPublishers()
    publishers = string_utils.build_input_options(self, publishers)
    self.choice = input("And who published this book?\n" + publishers)
    self.store["publishers"] = self.grabId()

    # CREATE NEW BOOK WITH AUTHOR

def update_book(self):
    self.choice = input("Select a book you would like to update\n")
    books = fetchProcedures.fetchBooks()
    books = string_utils.build_input_options(self, books)
    self.choice = input("Which book do you want to update?\n" + books)
    self.store["bookId"] = self.grabId()
    

def delete_book(self):
    self.choice = input("Select the book you would like to delete\n")
    books = fetchProcedures.fetchBooks()
    books = string_utils.build_input_options(self, books)
    self.choice = input("Which book do you want to update?\n" + books)
    self.store["bookId"] = self.grabId()

