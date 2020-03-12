import borrower_questions

# print(borrower_questions.__dict__)


for name, val in borrower_questions.__dict__.items():
    if callable(val):
        print(val)


questions = {
    "user": [],
    "librarian": [],
    "admin": []
}

