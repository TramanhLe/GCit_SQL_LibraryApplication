import questions
import user
# Create a library management application on the Command Line which will follow the following protocol.

# User is first presented the following options:

# MAIN:   
#     Welcome to the GCIT Library Management System. 
#     Which category of auser are you

#     1)Librarian
#     2)Administrator
#     3)Borrower
   


dummy_input = "borrower"

test_case = user.User(dummy_input, questions.question_bank["start"][dummy_input], questions.question_bank[dummy_input])
test_case()







