import borrower_questions


for name, val in borrower_questions.__dict__.iteritems():
    print(name)


questions = {
    "user": [],
    "librarian": [],
    "admin": []
}

