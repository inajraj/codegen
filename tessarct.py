

import os


BasePath = 'C:/Users/User1/Documents/codegen/input'


for filename in os.listdir(BasePath):
    print(filename)
    inputPath = BasePath + '/' + filename
    outputPath = BasePath + '/' + filename[:-4]
    
    cmd = "tesseract " + inputPath + " " + outputPath + " --oem 1 -l eng"
    os.system(cmd)