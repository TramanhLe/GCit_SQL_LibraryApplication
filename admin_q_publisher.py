import string_utils
import updateProcedures
import fetchProcedures

def start(self):
    self.choice = input("1) Add \n2) Update\n3) Delete Publisher\n")
        if self.choice == "1":
            print("Add Publisher")
        elif self.choice == "2":
            print("Update an existing Publisher")
        elif self.choice == "3":
            print("Delete an existing Publisher")


def add_publisher(self):
    add_data = {}
    add_data["name"] = input("What is the name of the publisher you wish to add?\n")
    add_data["address"] = input("What is the address of this publisher?")
    add_data["phone"] = input("What is the phone number of this publisher?")

    # Build function to display what they have written, so we can them confirm it is good
    self.choice = input("Does that look right to you?\n1) Yes\n2) No")
    if self.choice == "1":
        print("Added new publisher")
        self.complete = True
    elif self.choice == "2":
        add_publisher()
    pass

def update_publisher(self):
    pass

def delete_publisher(self):
    pass