import mysql.connector

def runScript(str, mydb):

    mycursor = mydb.cursor()

    mycursor.execute(str)

    mydb.commit()