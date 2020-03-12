import borrower_questions

# print(borrower_questions.__dict__)

questions = {
    "borrower": [],
    "librarian": [],
    "admin": []
}

for name, val in borrower_questions.__dict__.items():
    if callable(val):
        questions["borrower"].append(val)



