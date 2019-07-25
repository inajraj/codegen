from __future__ import print_function
import pickle
import os.path
import sys

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from generateRules import RunRulesGenerator
from generateScreens import RunScreenGenerator
from generateValidateSnippets import RunScreenValidationsGenerator
from generateDDL import RunDDLGenerator

from commonUtils import doSelect, doInput, doSel2, doInput2, doSelandInput, doInputandSel

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
#SPREADSHEET_ID = '1WmIHC5ic4IFE4b5uEXgfxEXm1GW-I7aW80xKS7rDcsA'
SPREADSHEET_ID = '1XV9F3FFtydBnTGY5_1V-cqEqnEBngwAD4VI2_daxxOs'   
RANGE_NAME = 'Master'

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

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

    #Over all master sheet has all the code gen projects .. we need to find the
    #code gen project which is having Y

    if not values:
        print('No data found.')
    else:
        for metaRow in values:
            if (metaRow[2] == 'Y'):
                sheetID = metaRow[1]
                RunMasterSheet(sheetID, "Master", sheet)
    
           
def RunMasterSheet(SHEET_ID, RANGE_NAME, sheet):
    # here we are opening the master sheet of the project where various 
    # sheets are listed for automation (screens, rules etc)
    
    result = sheet.values().get(spreadsheetId=SHEET_ID,
                                range=RANGE_NAME).execute()
    values = result.get('values', [])
    if not values:
        print('No data found.')
    else:
        for metaRow in values:
            print(metaRow[0], metaRow[1], metaRow[2])
            if (metaRow[3] == 'Y'):
                sheetId = metaRow[1]
                rangeName = metaRow[2]
                genType = metaRow[0]
                if (genType == 'Rules'):
                   RunRulesGenerator(sheet, sheetId, rangeName)
                elif (genType == 'Screens'):
                   RunScreenGenerator(sheet, sheetId, rangeName)
                elif (genType == 'ScreenValidations'):
                    RunScreenValidationsGenerator(sheet, sheetId, rangeName)
                elif  (genType == 'Tables'):
                    RunDDLGenerator(sheet, sheetId, rangeName)
                    
           
                            
        
if __name__ == '__main__':
    main()