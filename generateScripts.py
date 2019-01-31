from __future__ import print_function
import pickle
import os.path
import sys

from datetime import date

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from commonUtils import doSelect, doInput, doSel2, doInput2, doSelandInput, doInputandSel

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
#SPREADSHEET_ID = '1WmIHC5ic4IFE4b5uEXgfxEXm1GW-I7aW80xKS7rDcsA'
SPREADSHEET_ID = '11TbcyAGEpZv0hqNJd5En8HRGG5yF1MBIjnC9EcE_pX4'   
RANGE_NAME = 'Screens'

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

sfile = open("snippets.js","a+")

def createLoadDataSnippets(controlInfo):
    sfile.write("$('#" + controlInfo[2] + "').val(myObj['" + controlInfo[2]+"']);\n")

def createSaveFormCodeSnippets(controlInfo):
    sfile.write("if ($('# " + controlInfo[2] + "').val().trim() != \"\")")
    sfile.write("\n\tmyObj['" + controlInfo[2]+"'] = $('#" + controlInfo[2] + "').val();\n")

def createValidationScriptText(controlInfo,f, blankFlag):
    #script to check valid input is there
    if (controlInfo[1] == 'T'):
        if (blankFlag == "Y"):
            f.write(("if (!$('#" + controlInfo[2] + "').val().match('^[a-zA-Z]{3,16}$') ) {" +
            " \nalert(#'That is not a valid " + controlInfo[2] + " ');" +
            " \n}\n"))
        else:
             f.write(("if ($('#" + controlInfo[2] + "').val().trim() != "" && !$('#" + controlInfo[2] + "').val().match('^[a-zA-Z]{3,16}$') ) {" +
            " \nalert('That is not a valid " + controlInfo[2] + " ');" +
            " \n}\n"))

def generateInsertScript(tableRows, tableName):

    str = "Insert into "+ tableName + " ("
    strValues = " Values ('"
    for row in tableRows:
        if len(row) > 0:
            firstControl = row[0].split('~')
            if len(row) > 1:
                #we have two controls in the same ro
                secondControl = row[1].split('~')
                str = str + firstControl[2] +","
                str = str + secondControl[2] +","

                strValues = strValues + "\" . $results['" + firstControl[2] + "'] . \"','"
                strValues = strValues + "\" . $results['" + secondControl[2] + "'] . \"','"
            else:
                str = str + firstControl[2] +","
                strValues = strValues + "\" . $results['" + firstControl[2] + "'] . \"','"
    
    str = str[:-1] + ") "
    strValues = strValues[:-2] + ")"
    sfile.write (str + strValues)
    
def generateUpdateScript(tableRows, tableName, updateKey):

    strValues = "Update "+ tableName + " SET "
    for row in tableRows:
        if len(row) > 0:
            firstControl = row[0].split('~')
            if len(row) > 1:
                #we have two controls in the same ro
                secondControl = row[1].split('~')
                strValues = strValues + firstControl[2] + " = '\" . $results['" + firstControl[2] + "'] . \"',"
                strValues = strValues + secondControl[2] + " = '\" . $results['" + secondControl[2] + "'] . \"',"
            else:
                strValues = strValues + firstControl[2] +" = '\" . $results['" + firstControl[2] + "'] . \"',"
    
    
    strValues = strValues[:-1] + " Where " + updateKey + " = '\" . $results['" + updateKey + "'] . \"'\";"
    sfile.write (strValues)

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_id.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range=RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        for metaRow in values:
            res=sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range=metaRow[0]).execute()
            tablerows = res.get('values', [])
            #generateInsertScript(tablerows,metaRow[0])
            generateUpdateScript(tablerows,metaRow[0],"EmpID")
            print(metaRow[0])
            if (metaRow[1] == 'Y'):
                #f= open(metaRow[0] + "-auto-script.js","w")
                for tdrow in tablerows:
                    print(tdrow, len(tdrow))
                    if len(tdrow) > 0:
                        firstControl = tdrow[0].split('~')
                        if len(tdrow) > 1:
                            #we have two controls in the same row
                            secondControl = tdrow[1].split('~')
                            #createValidationScriptText(firstControl,f,"N")
                            #createValidationScriptText(secondControl,f,"N")
                            #createSaveFormCodeSnippets(firstControl)
                            #createSaveFormCodeSnippets(secondControl)
                            #createLoadDataSnippets(firstControl)
                        else:
                            #createValidationScriptText(firstControl,f,"Y")
                            #createSaveFormCodeSnippets(firstControl)
                            #createLoadDataSnippets(firstControl)
                            print("D")
               # f.close()    
                            
        
if __name__ == '__main__':
    main()