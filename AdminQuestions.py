import string_utils
import updateProcedures
import fetchProcedures


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
                print("Adding publisher")
            elif int(ans)==2:
                print("Updating publisher")
            elif int(ans)==3:
                print("Delete Publisher")
            else:
                print("Invalid input type 'quit' to go back")
    #library branch
    elif int(ans)==3:
        while True:
            ans=input("1) Add Library Branch\n2) Update Library Branch\n3) Delete Library Branch")
            if ans=="quit":
                break
            elif int(ans)==1:
                print("Adding Library Branch")
            elif int(ans)==2:
                print("Updating Library Branch")
            elif int(ans)==3:
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
