import fetchProcedures
import updateProcedures
import start_questions
import questions

def lib_question_one(self):
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
    str_branch = (''.join(branches[int_choice]))
    self.id = fetchProcedures.fetchBranchIdByName(str_branch)
    self.choice = input("Press 1) Update the details of the Library\nPress 2) Add copies of Book to the Branch\n : ")
    if self.choice == "1":
        print(f'You have chosen to update the Branch with Branch Id: {self.id} and Branch Name: {str_branch}.')
        new_branch_name = input(f"Please Enter New Branch Name for {str_branch}\n:")
        if new_branch_name != ""
        updateProcedures.updateBranchName(f"{self.id[0]}",f"{str_branch}",f"{new_branch_name}")
        print(f"{self.id[0]}", f"{str_branch}", f"{new_branch_name}")
        elif
    elif self.choice == "2":
