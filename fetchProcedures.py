import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rootadmin123",
    auth_plugin='mysql_native_password',
    database="library")
myCursor = mydb.cursor()

results=[]

def fetchBranchs():
    myCursor.callproc('sp_showAllBranch')
    for x in myCursor.stored_results():
        results=x.fetchall()
    return results

def fetchBranchInfo():
    myCursor.callproc('sp_showAllBranch')
    for x in myCursor.stored_results():
        results=x.fetchall()
    return results



