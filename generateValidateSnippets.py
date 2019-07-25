from __future__ import print_function
import pickle
import os.path
import sys

from datetime import date

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from commonUtils import doSelect, doInput, doSel2, doInput2, doSelandInput, doInputandSel



operatorDict = {} 

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)


f = open("snippets.js","a+")

def getCreds():
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
    return creds

def getOperatorTexts(results):
    for row in results:
        operatorDict[row[0]] = row[1]


def RunScreenValidationsGenerator(sheet, sheetId, rangeName):

    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = getCreds()
   

    result = sheet.values().get(spreadsheetId=sheetId,
                                range='OperatorsText').execute()
    results = result.get('values', [])

    getOperatorTexts(results)
    

    result = sheet.values().get(spreadsheetId=sheetId,
                                range=rangeName).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        #the operator text in a dictionary
        for metaRow in values:
            print(metaRow)
            res=sheet.values().get(spreadsheetId=sheetId,
                                range=metaRow[0]).execute()
            tablerows = res.get('values', [])
            if (metaRow[1] == 'Y'):
                for tdrow in tablerows:
                    print(tdrow, len(tdrow))
                    if len(tdrow) > 0:
                        createValidationScript(tdrow)
                        
    f.close()

def createValidationScript(tdrow):

    #check if the Name validation
    if (tdrow[0] == 'Name'):
        createNameCheckingScript(tdrow)
    elif (tdrow[0] == 'Date'):
        createDateConditionScript(tdrow)
    elif (tdrow[0] == 'MobileNumber'):
        createMobileNumberCheckingScript(tdrow)
    elif (tdrow[0] == 'CombineCondition'):
        createCombineConditionScript(tdrow)
    elif (tdrow[0] == 'CombineVal'):
        createCombineValScript(tdrow)
    elif (tdrow[0] == 'CombineBlank'):
        createCombineBlankScript(tdrow)
    elif (tdrow[0] == 'EitherBlank'):
        createEitherBlankScript(tdrow)
        
def createCheckName(f):
    f.write("\nfunction checkName(controlName, FieldName, blankFlag) {")
    f.write("\n\tif (blankFlag != 'Y')  {")
    f.write("\n\t\tif ( $('#'+controlName).val() == '') {")
    f.write("\n\t\t\tbootbox.alert(FieldName + ' can not be blank'); ")
    f.write("\n\t\t\treturn false;")
    f.write("\n\t\t}")
    f.write("\n\t}")
    f.write("\n\tif( /^[a-zA-Z0-9- ]*$/.test( $('#'+controlName).val() ) == false ) {")
    f.write("\n\t\tbootbox.alert(FieldName + ': input is not alphanumeric');")
    f.write("\n\t\treturn false;")
    f.write("\n\t}")
    f.write("\n\treturn true;")
    f.write("\n}")

def createNameCheckingScript(tdrow):
    #this script will generate a code snippet which will call
    # checkName function already created by 'createCheckName'
    f.write("\n\nif (!checkName('" + tdrow[1] + "', '" + tdrow[2] + "'))")
    f.write("\n\treturn false;") 

def createDateConditionScript(tdrow):
    #need to generate the script for checking the date is falling between min and max values
    #need to create mindate and maxdate variables using the min n max values
    f.write("\n\nvar dte = new Date($('" + tdrow[1] + "').val);")
    f.write("\nvar minDate = new Date();")
    f.write("\nvar maxDate = new Date();")
    f.write("\nminDate.setDate(minDate.getDate() - " + tdrow[3] +");")
    f.write("\nmaxDate.setDate(maxDate.getDate() - " + tdrow[4] +");")
    f.write("\nvar res = validateDate(dte,minDate,maxDate)")
    f.write("\nif (res == -1) ")
    f.write("\n\tbootbox.alert('" + tdrow[2]  + " is lower than Minium Date allowed');")
    f.write("\nif (res == 1) ")
    f.write("\n\tbootbox.alert('" + tdrow[2]  + " is greater than Maximum Date allowed');")

def createMobileNumberCheckingScript(tdrow):
    #check for mobile number validation
    f.write("\n\nvar regex=/^(\\+\\d{1,3}[- ]?)?\\d{10}$/;")
    f.write("\nif (!$(" + tdrow[1] + ").val().match(regex)) ")
    f.write("\n\tbootbox.alert('" + tdrow[2]  + " is not a valid Mobile Number');")
    
def createCombineConditionScript(tdrow):
    #two fileds are compared using the operator
    f.write("\n\nif (!$(" + tdrow[1] + ").val() " + tdrow[3] + "  $(" + tdrow[4] + ").val())")
    f.write("\n\tbootbox.alert('" + tdrow[2] + " should be " + operatorDict[tdrow[3]] + " " + tdrow[5] +"');")

def createCombineValScript(tdrow):
    f.write("\n\nif ($(" + tdrow[1] + ").val() == " + tdrow[3] + " && ($(" + tdrow[4] + ").val() == null || $(" + tdrow[4] + ").val()  ==''))")
    f.write("\n\tbootbox.alert('" + tdrow[2] + " should not be -- " + tdrow[3] +" -- if " + tdrow[5] +" is empty');")

def createCombineBlankScript(tdrow):
    f.write("\n\nif ($(" + tdrow[4] + ").val() != '' && ($(" + tdrow[1] + ").val() == null || $(" + tdrow[1] + ").val()  ==''))")
    f.write("\n\tbootbox.alert('" + tdrow[2] + " should not be blank if " + tdrow[5] +" has value');")

def createEitherBlankScript(tdrow):
    f.write("\n\nif (($(" + tdrow[1] + ").val() == null || $(" + tdrow[1] + ").val()  =='') && ($(" + tdrow[4] + ").val() == null || $(" + tdrow[4] + ").val()  ==''))")
    f.write("\n\tbootbox.alert(' Either " + tdrow[2] + " or " + tdrow[5] +" should have value');")

