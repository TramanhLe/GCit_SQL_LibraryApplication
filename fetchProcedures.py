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
def fetchBranchs():
    myCursor.callproc('sp_showAllBranch')
    for x in myCursor.stored_results():
        results=x.fetchall()
    return results

def validateCardNo(input):
    myCursor.callproc('sp_validateCardNo',[input])
    for x in myCursor.stored_results():
        results=x.fetchone()
    return results

def fetchBorrowerBooks(input):
    myCursor.callproc('sp_fetchBorrowerBooks',[input])
    for x in myCursor.stored_results():
        results=x.fetchall()
    return results

def fetchBranchIdByName(input):
    myCursor.callproc('sp_fetchBranchIdByName',[input])
    for x in myCursor.stored.results():
        results=x.fetchone()
    return results



# Not done
def fetchBranchInfo():
    #fetch branch info
    myCursor.callproc('sp_showAllBranch')
    for x in myCursor.stored_results():
        results=x.fetchall()
    return results



