import questions
# Create a library management application on the Command Line which will follow the following protocol.

# User is first presented the following options:

# MAIN:   
#     Welcome to the GCIT Library Management System. 
#     Which category of auser are you

#     1)Librarian
#     2)Administrator
#     3)Borrower


# LIBRARIAN
#     LIB1:
#         1)Enter Branch you manage
#         2)Quite to previous (should take you menu MAIN)
#         <take input>
        
#         For Option 1, Give a list of Library branches using the names or locations like this:
#             LIB2:
#                 1)University Library, Boston 
#                 2)State Library, New York
#                 3)Federal Library, Washington DC
#                 4)County Library, McLean VA 
#                 5)Quit to previous (should take you menu LIB1)
#                 <take input>

#                 The user will only pick the number in the above list and you should figure out 
#                 which branch he is referring. Based on the selection, the next list would be:
#                     LIB3:
#                         1)Update the details of the Library 
#                         2)Add copies of Book to the Branch
#                         3)Quit to previous (should take you menu LIB2)






































class User:
    def __init__(self, user_role, first_path_question, user_specific_path):
        self.role = user_role
        self.id = ''
        self.track = 0
        self.track_list = []
        self.track_list_glossary = user_specific_path
        self.initial_question = first_path_question
        self.choice = ''


    def next(self):
        self.track += 1

    def prev(self):
        self.prev -=  1
    def home(self):
        self.track = 0

    def track_switch(self):
        self.initial_question(self)
        self.track_list = self.track_list_glossary[int(self.choice)]

    def __call__(self):
        self.engine()

    def engine(self):
        self.track_switch()
        
        
        while self.track <= len(self.track_list):
            self.track_list[self.track](self)
        print("Go to main")    

    # def question_one(self):
    #     self.id = input("Enter your card number.\n")
    #     # Valid card number check here
    #     card = True
    #     if card == True:
    #         self.choice = input("1) Check out a book\n 2) Return a book\n")
    #         self.next()
    #     else:
    #         pass
    
    # def question_two(self):
    #     if self.choice == "1":
    #         # Get branches here
    #         branches = ["New York", "New Mexico", "New Hampshire", "New Zealand"]
    #         for i, count in enumerate(branches):
    #             print(count)
    #         branch = input(""" Which branch do you want 
    #                           to check out from?\n 1) {branches[0]}\n
    #                            2) {branches[1]}\n
    #                             3) {branches[2]}""")
    #         self.next()
    #     elif self.choice == "2": 
    #         # Get books this borrower has checked out
    #         books = ["Romeo","Juliet","Ron Howard"]
    #         self.next()







dummy_input = "borrower"

test_case = User(dummy_input, questions.question_bank["start"][dummy_input], questions.question_bank[dummy_input])
test_case()


# def main():
#     print("Welcome to the GCIT Library Management System")
#     role = input("Which category of user are you?\n 1)Librarian\n 2)Administrator\n 3)Borrower\n ")
#     if role == "1":
#         librarian_path()
#     if role == "2":
#         borrower_path()

# def librarian_path(): 
#     choice = input("1)Enter Branch you manage\n 2) Quite to previous \n ")
#     if choice == "1":
#         branch = ("1)University Library, Boston \n 2)State Library, New York\n 3)Federal Library, Washington DC\n 4)County Library, McLean VA \n 5)Quit to previous")
#     else:
#         print("Go back to menu")

# # "1)University Library, Boston \n 2)State Library, New York\n 3)Federal Library, Washington DC\n 4)County Library, McLean VA \n 5)Quit to previous"
# def borrower_path():
#     cardNo = input("Enter your card number.\n")
#     # Valid card number check here
#     card = True
#     if card == True:
#         choice = input("1)Check out a book\n 2) Return a book\n")
#         borrower_path_2(carNo, choice)

# def borrower_path_2(cardNo, choice):
#     if choice == "1":
#         branch = input("Which branch do you want to check out from?")
#     elif choice = "2": 
#         # Get books this borrower has checked out
#         books = ["Romeo","Juliet","Ron Howard"]




