import questions
import user
import admin
# Create a library management application on the Command Line which will follow the following protocol.

# User is first presented the following options:

# MAIN:   
#     Welcome to the GCIT Library Management System. 
#     Which category of auser are you

#     1)Librarian
#     2)Administrator
#     3)Borrower
   

print("Welcome to the GCIT Library Management System!\n")
print("What kind of user are you?\n")
choice = input("1)Librarian\n2)Borrower\n3)Administrator\n")
if choice == "1":
    user_type = "librarian"
elif choice == "2":
    user_type = "borrower"
elif choice == "3":
    user_type = "administrator"


if choice =="1" or choice == "2":
    test_case = user.User(user_type, questions.question_bank["start"][user_type], questions.question_bank[user_type])
    test_case()
elif choice == "3":
    test_case = admin.Admin()
    test_case()







