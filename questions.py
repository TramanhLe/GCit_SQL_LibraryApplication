import borrower_q_check_out
import borrower_q_return
import start_questions
import admin_q_book_and_author

# Each int : array within the values of borrower, librarian, and admin
question_bank = {
    "start": {
        "borrower": start_questions.borrower_question_one,
        "admin": start_questions.admin_question_one
    },
    "borrower": {
        # check_out
        1: [],
        # return
        2: [],
    },
    "librarian": {
        1: [],
        2: []
    },
    "admin": {
        #Book and Author
        1: [],
        #Publishers
        2: [],
        #Library Branches
        3: [],
        #Borrowers
        4: [],
        #Over ride due date for a Book Loan
        5: [],
        #Exit
        6:[]
    }
}



# For loop for each "line of questioning"
for name, val in borrower_q_check_out.__dict__.items():
    if callable(val):
        question_bank["borrower"][1].append(val)

for name, val in borrower_q_return.__dict__.items():
    if callable(val):
        question_bank["borrower"][2].append(val)



# For loop for each "line of questions" for admin
for name, val in admin_q_book_and_author.__dict__.items():
    if callable(val):
        question_bank["admin"][1].append(val)

