import string_utils
def question_one(self):
    books = ["book1", "book2", "book2"]
    books = string_utils.build_input_options(books)
    self.choice = input("Which book would you like to return?\n" + books)
    self.next()