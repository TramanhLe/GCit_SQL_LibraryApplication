import string_utils
import updateProcedures
import fetchProcedures

def start(self):
    print("What would you like to do?\n")
    self.choice = input("1) Add/Update/Delete Book\n2) Add/Update/Delete Author\n")
    if self.choice == "1":
        self.choice = input("1) Add Book\n2) Update Book\n3) Delete Book\n")
        if self.choice == "1":
            print("Add book")
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
    self.update_data["title"] = input("What is the title of the book you want to add?\n")
    self.update_data["author"] = input("Who authored this book?\n")
    # CREATE NEW BOOK WITH AUTHOR

def update_book(self):
    self.choice = input("Select a book you would like to update\n")
    # GET ALL BOOKS

def delete_book(self):
    self.choice = input("Select the book you would like to delete\n")
    # GET ALL BOOKS HERE