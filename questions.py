import borrower_q_check_out
import borrower_q_return
import librarian_questions
import start_questions

# Each int : array within the values of borrower, librarian, and admin
question_bank = {
    "start": {
        "borrower": start_questions.borrower_question_one,
        "librarian": start_questions.lib_question_one,
    },
    "borrower": {
        # check_out
        1: [],
        # return
        2: [],
    },
    "librarian": {
        1: [],
        2: [],
    },
    "admin": {
        1: [],
        2: [],
    }
}



# For loop for each "line of questioning"
for name, val in borrower_q_check_out.__dict__.items():
    if callable(val):
        question_bank["borrower"][1].append(val)

for name, val in borrower_q_return.__dict__.items():
    if callable(val):
        question_bank["borrower"][2].append(val)

for name, val in librarian_questions.__dict__.items():
    if callable(val):
        question_bank["librarian"][1].append(val)


