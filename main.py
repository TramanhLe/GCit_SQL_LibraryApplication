# DONT WORRY ABOUT THIS FOR NOW, I AM WORKING ON IT AND SHOULD HAVE KEPT IT IN ITS OWN BRANCH -HOFF

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



































# Some awesome and cool changes here





class Borrower:
    def __init__(self):
        self.id = ''
        self.track = 0
        self.track_list = []
        self.choice = ''


    def next(self):
        self.track + 1

    def prev(self):
        self.prev -  1
    def home(self):
        self.track = 0
    
    def __call__(self):
        self.engine()

    def engine(self):
        while self.track < 2:
            self.track_list[self.track]
        print("Go to main")    






# def main():
#     print("Welcome to the GCIT Library Management System")
#     role = input("Which category of user are you?\n 1)Librarian\n 2)Administrator\n 3)Borrower\n ")
#     if role == "1":
#         librarian_path()
#     if role == "2":
#         borrower_path()







