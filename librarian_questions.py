def lib_question_one(self):
    if self.choice == "1":
        res = (fetchProcedures.fetchBranchs())
        out = ""
        for i, val in enumerate(res):
            output = f"{i}) {val}\n"
            out += output
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
        new_branch_name = input(f"Please Enter New Branch Name for {str_branch}\n or enter N/A for no change:")
        if len(new_branch_name) > 0:
            updateProcedures.updateBranchName(f"{self.id[0]}",f"{str_branch}",new_branch_name)
        else:
             print('No Changes for Branch Name')
        pass
        new_address = input(f'Please enter new branch address for {new_branch_name} or enter N/A for no change:\n')
        if len(new_address) > 0:
            updateProcedures.updateBranchAddress(f"{self.id[0]}",new_address)
            self.prev()
        else:
            print('No Changes for Branch Address')
    if self.choice == "2":
        self.next()


def lib_update_address(self):
    print('yay')
