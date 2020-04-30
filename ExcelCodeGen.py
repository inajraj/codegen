

import openpyxl
from generateDDL import RunDDLGenerator

# Give the location of the file 
path = "C:\\Users\\user1\\Downloads\\Tables.xlsx"
  
# To open the workbook  
# workbook object is created 
wb = openpyxl.load_workbook(path) 
  
# Get workbook active sheet object 
# from the active attribute 
sheet = wb['MetaData']
  
# Cell objects also have row, column,  
# and coordinate attributes that provide 
# location information for the cell. 
  
# Note: The first row or  
# column integer is 1, not 0. 
  
# Cell object is created by using  
# sheet object's cell() method. 
rowCount = sheet.max_row
#print(sheet['B' + str(2)].value)

i = 2
while i <=  rowCount:
    if (sheet['C' + str(i)].value == 'Y' or sheet['D' + str(i)].value == 'Y'):
        sheetID = sheet['B' + str(i)].value
        print(sheetID)
        RunDDLGenerator(wb,  sheet['B' + str(i)].value, sheet['C' + str(i)].value, sheet['D' + str(i)].value)
    i = i + 1
        
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
           