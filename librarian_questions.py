import fetchProcedures
import start_questions
import questions

def lib_question(self):
    if self.choice == "1":
        res = (fetchProcedures.fetchBranchs())
        out = ""
        for i, val in enumerate(res):
            output = f"{i}) {val}\n"
            out += output
        self.choice = input("Please Select Branch number or q to quit to previous:\n" + out)
        self.next()

def lib_question_two(self):
    int_choice = int(self.choice)
    branches = (fetchProcedures.fetchBranchs())
    branches[int_choice]
    fetchProcedures.fetchBranchIdByName(branches[int_choice])
    
