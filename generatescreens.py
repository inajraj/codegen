from __future__ import print_function
import pickle
import os.path
import sys

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from commonUtils import doSelect, doInput, doSel2, doInput2, doSelandInput, doInputandSel



file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)



def createOneSet(firstControl,f):
    if  firstControl[1] == 'DD':
       doSelect(firstControl[0],firstControl[2],f)
    if  firstControl[1] == 'T' or firstControl[1] == 'DT':
       doInput(firstControl[0],firstControl[2], firstControl[1],f)
    

def createTwoSet(firstControl,secondControl,f):
    fcType = firstControl[1]
    scType = secondControl[1]
    if (fcType == "DD" and scType == "DD"):
        doSel2(firstControl[0],firstControl[2],secondControl[0],secondControl[2],f)
    elif (fcType == "DD" and (scType == "T" or scType == "DT")):
        doSelandInput(firstControl[0],firstControl[2],secondControl[0],secondControl[2],scType,f)
    elif ((fcType == "T" or fcType == "DT") and scType == 'DD'):
        doInputandSel(firstControl[0],firstControl[2],secondControl[0],secondControl[2],fcType,f)
    elif ((fcType == "T" or fcType == "DT") and (scType == 'DT' or scType == 'T')):
        doInput2(firstControl[0],firstControl[2],secondControl[0],secondControl[2],fcType, scType, f)
    



def RunScreenGenerator(sheetID, rangeName, sheet):
   

    # Call the Sheets API
    
    result = sheet.values().get(spreadsheetId=sheetID,
                                range=rangeName).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        for metaRow in values:
            res=sheet.values().get(spreadsheetId=sheetID,
                                range=metaRow[0]).execute()
            tablerows = res.get('values', [])
            print(metaRow[0])
            if (metaRow[1] == 'Y'):
                f= open(metaRow[0] + "-auto-screen.php","w")
                for tdrow in tablerows:
                    print(tdrow, len(tdrow))
                    if len(tdrow) > 0:
                        firstControl = tdrow[0].split('~')
                        if len(tdrow) > 1:
                            #we have two controls in the same row
                            secondControl = tdrow[1].split('~')
                            createTwoSet(firstControl, secondControl,f)
                        else:
                            createOneSet(firstControl,f)
                f.close()    
                        