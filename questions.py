import borrower_q_check_out
import borrower_q_return
import start_questions


question_bank = {
    "start": {
        "borrower": start_questions.borrower_question_one
    },
    "borrower": {
        # check_out
        0: [],
        # return
        1: []
    },
    "librarian": {
        0: [],
        1: []
    },
    "admin": {
        0: [],
        1: []
    }
}



# For loop for each "line of questioning"
for name, val in borrower_q_check_out.__dict__.items():
    if callable(val):
        question_bank["borrower"][0].append(val)

for name, val in borrower_q_return.__dict__.items():
    if callable(val):
        question_bank["borrower"][1].append(val)



