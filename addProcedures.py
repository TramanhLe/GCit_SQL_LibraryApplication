#Connection to DB
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rootadmin123",
    auth_plugin='mysql_native_password',
    database="library",
    autocommit=True)
myCursor = mydb.cursor()

def addBranch(branchName,branchAddress):
    myCursor.callproc('A_addBranch',[branchName,branchAddress])

def addBorrower(bName,bAddress,bPhone):
    myCursor.callproc('A_addBorrower',[bName,bAddress,bPhone])