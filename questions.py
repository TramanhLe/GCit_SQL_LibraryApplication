import borrower_questions
import librarian_questions

# print(borrower_questions.__dict__)

questions = {
    "borrower": [],
    "librarian": [],
    "admin": []
}

for name, val in borrower_questions.__dict__.items():
    if callable(val):
        questions["borrower"].append(val)

for name, val in librarian_questions.__dict__.items():
    if callable(val):
        questions["librarian"].append(val)

