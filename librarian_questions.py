import fetchProcedures
import updateProcedures
import start_questions
import string_utils
import questions

def lib_question_one(self):
    if self.choice == "1":
        res = (fetchProcedures.fetchBranchs())
        out = string_utils.build_input_options(self, res)
        self.choice = input("Select Branch Number or q to quit to previous:\n" + out)
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
        if len(new_branch_name) > 0:
            updateProcedures.updateBranchName(f"{self.id[0]}",f"{str_branch}",new_branch_name)
        else:
            print('nay')
