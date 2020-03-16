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

results=[]

#DONE

def deleteBranch(input):
    myCursor.callproc('sp_deleteLibraryBranch',[input])

def deleteBorrower(input):
    myCursor.callproc('sp_deleteBorrower',[input])