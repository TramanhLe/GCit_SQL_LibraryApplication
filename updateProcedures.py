#Connection to DB
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rootadmin123",
    auth_plugin='mysql_native_password',
    database="library")
myCursor = mydb.cursor()

results=[]

#Done
def updateBranchInfo(bName,bAdd,bId):
    myCursor.callproc('sp_updateLibraryBranch',[bName,bAdd,bId])
    print("Library branch has been updated")
    






#Not done