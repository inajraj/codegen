
import os
import shutil

from ImageConverter import ConvertImages

def createFolders(filepath,archive):
    #create new folders processed and output
    os.makedirs(filepath + "/" + archive + "/" + 'processed')
    os.makedirs(filepath + "/" + archive + "/" + 'output')

def tifConversion(filepath,archive):
    #conver the tiff files to jpg
    ConvertImages(filepath + "/" + archive)
    #after conversion remove the tiff files
    for filename in os.listdir(filepath + "/" + archive):
        if filename.endswith(".tif"):
            os.remove(filepath + "/" + archive + "/" + filename)

def copyFiles(sourcePath, destPath):
    shutil.copy(sourcePath, destPath)

def movefiles(sourcePath, destPath):
    #fullname = filepath + "/" + filename
    shutil.move(sourcePath, destPath)


files = [

'OEBS2701028ws92001.jpg',
'OEBS2701028ws92003.jpg',
'OEBS2701028ws92004.jpg',
'OEBS2701028ws92006.jpg',
'OEBS2701028ws92007.jpg',
'OEBS2701028ws92008.jpg',
'OEBS2701028ws92010.jpg',
'OEBS2701028ws92011.jpg',
'OEBS2701028ws92015.jpg',
'OEBS2701028ws92016.jpg',
'OEBS2701028ws92018.jpg',
'OEBS2701028ws92020.jpg',
'OEBS2701028ws92021.jpg',
'OEBS2701028ws92022.jpg',
'OEBS2701028ws92026.jpg',
'OEBS2701028ws92029.jpg',
'OEBS2701028ws92030.jpg',
'OEBS2701028ws92032.jpg',
'OEBS2701028ws92034.jpg',
'OEBS2701028ws92037.jpg',
'OEBS2701028ws92040.jpg',
'OEBS2701028ws92042.jpg',
'OEBS2701028ws92043.jpg',
'OEBS2701028ws92044.jpg',
'OEBS2701028ws92047.jpg',
'OEBS2701028ws92049.jpg',
'OEBS2701028ws92156.jpg',
'OEBS2701028ws92193.jpg',
'OEBS2701028ws92215.jpg'

]


filepath = 'C:/Users/User1/Downloads/HtmlConv'

archive = 'OEBS2701074'

#sourcePath = filepath + "/" + archive + "/processed"
#destPath = filepath + "/temp" 

#for filename in files:
#    copyFiles(sourcePath + "/" + filename,destPath)

createFolders(filepath, archive)

tifConversion(filepath, archive)




#     fullname = filepath + "/" + filename
#     shutil.move(fullname, 'C:\\Users\\User1\\Documents\\codegen\\input')