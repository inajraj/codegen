import mysql.connector

def runScript(str, mydb):

    print(str)

    mycursor = mydb.cursor()

    mycursor.execute(str)

    mydb.commit()