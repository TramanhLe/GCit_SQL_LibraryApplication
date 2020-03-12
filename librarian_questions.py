import fetchProcedures 

def lib(self):
    self.choice = input("1)Enter Branch you manage\n 2)Quite to previous\n" )
    if self.choice == "1":
        res = (fetchProcedures.fetchBranchs())
        out = ""
        for i, val in enumerate(res):
            output = f"{i}) {val}\n"
            out += output
        self.choice = input("Please Select Branch:\n" + out)
        if self.choice == f"{i}":
            print('yay')
        




