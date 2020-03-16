import string_utils
import updateProcedures
import fetchProcedures

def start(self):
    print("What would you like to do?\n")
    self.choice = input("1) Add \n2) Update\n3) Delete Publisher\n")
    if self.choice == "1":
        print("Add Publisher")
    elif self.choice == "2":
        print("Update an existing Publisher")
    elif self.choice == "3":
        print("Delete an existing Publisher")


def add_publisher(self):
    self.store["name"] = input("What is the name of the publisher you wish to add?\n")
    self.store["address"] = input("What is the address of this publisher?")
    self.store["phone"] = input("What is the phone number of this publisher?")

    # Build function to display what they have written, so we can them confirm it is good
    self.choice = input("Does that look right to you?\n1)Yes\n2)No")
    if self.choice == "1":
        print("Added new publisher")
    elif self.choice == "2":
        add_publisher()
    

def update_publisher(self):
    publishers = fetchProcedures.fetchBorrowers()
    publishers = string_utils.build_input_options(self, publishers)
    self.choice = input("Which publisher would you like to update?\n")
    
    self.store["name"] = input("What is the name of the publisher you wish to add?\n")
    self.store["address"] = input("What is the address of this publisher?")
    self.store["phone"] = input("What is the phone number of this publisher?")

    print("Updated publisher")
    # UPDATE PUBLISHER (name, address, phone)

def delete_publisher(self):
    publishers = fetchProcedures.fetchBorrowers()
    publishers = string_utils.build_input_options(self, publishers)
    self.choice = input("Which publisher would you like to delete?\n")
    
    print("Deleted publisher")
    # DELETE PUBLISHER BY ID HERE
