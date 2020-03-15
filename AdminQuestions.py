import string_utils
import updateProcedures
import fetchProcedures
import sys
sys.dont_write_bytecode = True


while True:
    ans=input("1) Add/Update/Delete Book and Author\n2) Add/Update/Delete Publishers\n3) Add/Update/Delete Library Branches\n4) Add/Update/Delete Borrowers\n5) Over-ride Due Date for a Book loan\n")
    if ans=="quit":
        print("end")
        break
    #Author and book
    elif int(ans)==1:
        #Book and author loop
        while True:
            ans=input("1) Add/Update/Delete Book\n2) Add/Update/Delete Author\n")
            if ans=="quit":
                break
            elif int(ans)==1:
                while True:
                    ans=input("1) Add Book\n2) Update Book\n3) Delete Book\n")
                    if ans=="quit":
                        break
                    elif int(ans)==1:
                        print("Adding book")
                    elif int(ans)==2:
                        print ("Updating book")
                    elif int(ans)==3:
                        print ("Deleting book")
                    else:
                        print("Invalid input type 'quit' to go back")
            elif int(ans)==2:
                while True:
                    ans=input("1) Add Author\n2) Update Author\n3) Delete Author\n")
                    if ans=="quit":
                        break
                    elif int(ans)==1:
                        print("Adding Author")
                    elif int(ans)==2:
                        print("Updating Author")
                    elif int(ans)==3:
                        print("Deleting Author")
                    else:
                        print("Invalid Input type 'quit' to go back")
            else:
                print("Invalid input type 'quit' to go back")
    #publisher 
    elif int(ans)==2:
        while True:
            ans=input("1) Add publisher\n2) Update Publisher\n3) Delete Publisher\n")
            if ans=="quit":
                break
            elif int(ans)==1:
                pubName=input("Enter the new publishers name?\n")
                if pubName=='quit':
                    break
                pubAddress=input("Enter the new publisher: "+pubName+" address\n")
                if pubAddress=='quit':
                    break
                pubPhoneNumber=input("Enter "+pubName+"'s phone number")
                if pubPhoneNumber=='quit':
                    break
                # Insert adding publisher procedure here
                print("Adding publisher")
            elif int(ans)==2:
                #Insert fetch publisher procedure here
                pubChoice=input("Which publisher do you want to update? \n")
                if pubChoice=='quit':
                    break
                newPubName=input("Enter new publisher name\n")
                if newPubName=='quit':
                    break
                newPubAddress=input("Enter the new address for "+newPubName+":\n")
                if newPubAddress=='quit':
                    break
                #insert update publisher procedure here
                print("Updating publisher")
            elif int(ans)==3:
                #insert fetch publisher procedure here
                pubChoice=input("Which publisher do you want to delete?\n")
                if pubChoice=='quit':
                    break
                #insert fetch publisher id by name here
                #insert delete publisher procedure here
                print("Delete Publisher")
            else:
                print("Invalid input type 'quit' to go back")
    #library branch
    elif int(ans)==3:
        while True:
            ans=input("1) Add Library Branch\n2) Update Library Branch\n3) Delete Library Branch\n")
            if ans=="quit":
                break
            elif int(ans)==1:
                newBranchName=input("What do you want to call this new branch?\n")
                if newBranchName=='quit':
                    break
                newBranchAddress=input("What is the address for the new branch "+newBranchName+"?\n")
                if newBranchAddress=='quit':
                    break
                #Enter adding library branch proceudre here
                print("Adding Library Branch")
            elif int(ans)==2:
                branchList=fetchProcedures.fetchBranchs()
                branches = string_utils.build_input_options(branchList)
                branchChoice = input(branches + "Which branch do you want to update?\n")
                if branchChoice=='quit':
                    break
                branchChoiceName=(''.join(branchList[int(branchChoice)-1]))
                branchId=fetchProcedures.fetchBranchIdByName(branchChoiceName)
                newBranchName = input("What is the new branch name?\n")
                if newBranchName=='quit':
                    break
                else:
                    newBranchAddress = input("What is the new address for "+newBranchName +"?\n")
                    if newBranchAddress=='quit':
                        break
                    else:
                        updateProcedures.updateBranchInfo(newBranchName,newBranchAddress,branchId[0])
            elif int(ans)==3:
                branchList=fetchProcedures.fetchBranchs()
                branches = string_utils.build_input_options(branchList)
                branchChoice = input(branches + "Which branch do you want to delete?\n")
                if branchChoice=='quit':
                    break
                branchChoiceName=(''.join(branchList[int(branchChoice)-1]))
                branchId=fetchProcedures.fetchBranchIdByName(branchChoiceName)
                #Delete branch procedure insert here
                print("Deleting Library Branch")
                
            else:
                print("Invalid input type 'quit' to go back")
    #borrowers
    elif int(ans)==4:
        while True:
            ans=input("1) Add Borrower\n2) Update Borrower\n3) Delete Borrower\n")
            if ans=="quit":
                break
            elif int(ans)==1:
                print("Adding Borrower")
            elif int(ans)==2:
                print("Updating Borrower")
            elif int(ans)==3:
                print("Deleting Borrower")
            else:
                print("Invalid input type 'quit' to go back")
    #override due date for a boook
    elif int(ans)==5:
        while True:
            print("Updating due date")
            break
    else:
        print("Invalid input type 'quit' to go back")
