from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import mysql.connector as mariadb


from dbUtils import runScript


def formFieldString(row):
    #get the row and form the field it could have the size or not a
    #also not null or not as well as primary key
    #all the int we need to automatically add unsigned
    #we also need to add auto_increment for the fields 'ID'
    finalStr = ""
    if (row[0]  == "ID"):
        finalStr = "`ID` "+ row[1] + ","
        return finalStr

    # need to see size is there or not
    

def RunDDLGenerator(sheet, sheetId, rangeName):    

    #get the db credentials
    result = sheet.values().get(spreadsheetId=sheetId,
                                range='DBCredentials').execute()
    values = result.get('values', [])
    for metaRow in values:
        if (metaRow[0] == 'host'):
            host = metaRow[1]
        elif (metaRow[0] == 'user'):
            user = metaRow[1]
        elif (metaRow[0] == 'password'):
            passwd = metaRow[1]
        elif (metaRow[0]=='database'):
            database = metaRow[1]

    print(host, user, passwd, database)
        
    mydb = mariadb.connect(
            host=host,
            user=user,
            passwd=passwd,
            database=database
        )

    result = sheet.values().get(spreadsheetId=sheetId,
                                range=rangeName).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        for metaRow in values:
            print (metaRow)
            res=sheet.values().get(spreadsheetId=sheetId,
                                range=metaRow[0]).execute()
            tablerows = res.get('values', [])
            print(metaRow[0])
            if (metaRow[1] == 'Y'):
                #create the table only if the indicator is Y
                #drop the table first
                str = "DROP TABLE IF EXISTS " + metaRow[0]
                runScript(str,mydb)
                finalStr = "CREATE TABLE `" + metaRow[0] + "` ("
                for tdrow in tablerows:
                    
                    finalStr  = finalStr + "`" + tdrow[0] + "` " + tdrow[1] + ","
                    print(tdrow)
                    
                    #check this row has primary key column
                    if ('PK' in tdrow[2]):
                        pkString = "PRIMARY KEY (`" + tdrow[0] + "`))"
                #need to add primary key - to check the loop again
                runScript(finalStr+pkString, mydb)
                print(finalStr+pkString)
            if (metaRow[2] == 'Y'):
                #load sample data 
                #truncate tables
                runScript("TRUNCATE TABLE `" + metaRow[0] + "`", mydb)

                #range name will be TableName.SampleData
                DataRange = metaRow[0] + ".SampleData"
                res=sheet.values().get(spreadsheetId=sheetId,
                                range=DataRange).execute()
                dataRows = res.get('values', [])
                
                #get the columns (max columns will do)
                nColumns = max(list(map(len,dataRows)))
                print(nColumns)
                queryList = []
                for i in range(nColumns):
                    instr = "INSERT INTO `" + metaRow[0] + "` ("
                    valstr = "VALUES ("
                    for fld in zip(tablerows,dataRows): # tuple of two lists
                        if i < len(fld[1]): #check if the second list has members for index i
                            if fld[1][i] != '' and 'ID' not in fld[1][i]: #it it is empty do not add the field
                                instr = instr + fld[0][0] + ","
                                if fld[0][2] == 'D':
                                    valstr = valstr + "'" +  fld[1][i] + "',"
                                else:
                                    valstr = valstr + "'" +  fld[1][i] + "',"
                    qStr = instr[:-1]+") " + valstr[:-1] + ")"
                    runScript(qStr, mydb)
                   

def generateInsertStringforPhp(sheet,sheetId,rangeName):
    
    result = sheet.values().get(spreadsheetId=sheetId,
                                range=rangeName).execute()
    values = result.get('values', [])
    
    for metaRow in values:
        res=sheet.values().get(spreadsheetId=sheetId,
                                range=metaRow[0]).execute()
        tablerows = res.get('values', [])
      
        if (metaRow[3] == 'Y'):
            qStr = "\"insert into " + metaRow[0] + "("
            for tdRow in tablerows:
                if ("NOT NULL" in tdRow[1]):
                    qStr = qStr + tdRow[0] + ","
                else:
                    qStr = qStr +  "\" . checkBlank(\""+ tdRow[0] + "\", $results) . \""
            qStr = qStr.rstrip(',') + ")" 
            qStr = qStr + " Values ('\""
            for tdRow in tablerows:
                if ("NOT NULL" in tdRow[1]):
                    qStr = qStr + " . $results[\'" + tdRow[0] + "\'] . \"','\""
                else:
                    qStr = qStr[:-3] +  "\" . removeBlank($results[\'" + tdRow[0] + "\']) . \" ,'\""

            qStr = qStr[:-5] + "\")\"" 
            print(qStr)

def generateUpdateStringforPhp(sheet,sheetId,rangeName):
    
    result = sheet.values().get(spreadsheetId=sheetId,
                                range=rangeName).execute()
    values = result.get('values', [])
    
    for metaRow in values:
        res=sheet.values().get(spreadsheetId=sheetId,
                                range=metaRow[0]).execute()
        tablerows = res.get('values', [])
        whereStr = ""
        if (metaRow[3] == 'Y'):
            qStr = "\"update " + metaRow[0] + " SET "
            for tdRow in tablerows:
                if ("PK" in tdRow[2]):
                    whereStr = ". \" where " + tdRow[0] + " = '\" . $results[\'" + tdRow[0] + "\'] . \"'\" "
                if ("NOT NULL" in tdRow[1]):
                    qStr = qStr  + tdRow[0] +  " = '\" . $results[\'" + tdRow[0] + "\'] . \"', "
                else:
                    qStr = qStr +  "\" . checkBlank(" + tdRow[0] + ", $results[\'" + tdRow[0] + "\']) .\" "
            qStr = qStr[:-3] + "'\" " + whereStr
            
            print(qStr)

     