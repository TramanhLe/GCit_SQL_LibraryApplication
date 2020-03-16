import string_utils
import updateProcedures
import fetchProcedures

def start(self):
    print("What would you like to do?\n")
    self.choice = input("1) Add/Update/Delete Book\n2) Add/Update/Delete Author\n")
    if self.choice == "1":
        self.choice = input("1) Add Book\n2) Update Book\n3) Delete Book\n")
        if self.choice == "1":
            add_book(self)
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


def add_book(self):
    self.store["title"] = input("What is the title of the book you want to add?\n")

    authors = fetchProcedures.fetchAuthors()
    authors = string_utils.build_input_options(self, authors)
    self.choice = input("Who authored this book?\n" + authors)
    self.store["author"] = self.grabId()

    publishers =  fetchProcedures.fetchPublishers()
    publishers = string_utils.build_input_options(self, publishers)
    self.choice = input("And who published this book?\n" + publishers)
    self.store["publisherId"] = self.grabId()

    # CREATE NEW BOOK WITH AUTHOR

def update_book(self):
    books = fetchProcedures.fetchBooks()
    books = string_utils.build_input_options(self, books)
    self.choice = input("Which book do you want to update?\n" + books)
    self.store["bookId"] = self.grabId()

    self.store["new_title"] = input("What do you want the new title to be?\n")
    publishers = fetchProcedures.fetchPublishers()
    publishers = string_utils.build_input_options(self, publishers)
    self.choice = input("Who should the new publisher be?\n")
    self.store["new_pub_id"] = self.grabId()

    # UPDATE BOOK BY ID   (new_title, new_pub_id)
    

def delete_book(self):
    books = fetchProcedures.fetchBooks()
    books = string_utils.build_input_options(self, books)
    self.choice = input("Which book do you want to delete?\n" + books)
    self.store["bookId"] = self.grabId()

    # DELETE BOOK BY ID

def add_author(self):
    self.store["authorName"] = input("What is the name of the new author?\n")

    # INSERT AUTHOR (authorName)

def update_author(self):
    authors = fetchProcedures.fetchAuthors()
    authors = string_utils.build_input_options(self, authors)
    self.choice = input("Which author would you like to update?\n")
    self.store["authorId"] = self.grabId()

    self.store["authorName"] = input("What would you like to change the author's name to?\n")

    # UPDATE AUTHOR BY ID (authorId, authorName)


def delete_author(self):
    authors = fetchProcedures.fetchAuthors()
    authors = string_utils.build_input_options(self, authors)
    self.choice = input("Which author would you like to delete?\n")
    self.store["authorId"] = self.grabId()

    # DELETE AUTHOR BY ID (authorId)
