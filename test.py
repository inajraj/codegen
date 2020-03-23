import gspread
from oauth2client.service_account import ServiceAccountCredentials
from generateDDL import RunDDLGenerator

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_id.json', scope)



client = gspread.authorize(creds)
sht1 = client.open_by_key('1oa2d--UTwdecSPrX1MKWIjsqHOCh7ULp657RkFLaap0')

wk = sht1.worksheet('MetaData')

val = wk.cell(2, 2).value
print (val)

values_list = wk.col_values(3)
print(values_list)

for i in range(len(values_list)):
    if values_list[i] == 'Y':
        sheetID = wk.cell(i+1,2).value
        RunDDLGenerator(sht1, wk.cell(i+1,2).value, wk.cell(i+1,3).value, wk.cell(i+1,4).value)
        #RunMasterSheet(sheetID, "Master", client)

def RunMasterSheet(SHEET_ID, RANGE_NAME, client):
    # here we are opening the master sheet of the project where various 
    # sheets are listed for automation (screens, rules etc)
    print(RANGE_NAME)
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
                    generateInsertStringforPhp(sheet,sheetId, rangeName)
                    generateUpdateStringforPhp(sheet,sheetId, rangeName)
           