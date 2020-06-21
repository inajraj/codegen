import os
import shutil
import time

from  xltodict import replaceWords, loadDictionary

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'client_id.json'

def writeToFile(itemList, filename):
    with open(filename, "w",encoding="utf-8") as f:
        f.write("\n".join(itemList))
        


if __name__ == '__main__':


    df = loadDictionary()
    BasePath = 'C:/Users/User1/Downloads/HtmlConv/OEBS2701056/output'
    inputPath = BasePath + '/input'
    outputPath = BasePath + '/output'
    #move the firstfile from basepath to inputpath

    files = []

    files =  open(BasePath + "/"+ "OEBS2701056ws96498.txt", 'r',encoding="utf-8").read().split('\n')
    
    #detect_text('OEBS2701026ws91504.jpg')
    for index, value  in enumerate(files):
        files[index] = replaceWords(value,df)
        print(files[index])
        
    
    writeToFile(files, "temp.txt")

   
    #for filename in os.listdir(BasePath):
        #make sure file does not appear in the list
        
        #if filename not in files:
        #if filename.endswith(".jpg"): #and not filename in files:
            #print(filename)
            #move it to processed foler
            #shutil.move(BasePath + "/" + filename, inputPath + "/" + "processed")
            #time.sleep(10)
            #files.append(filename)
                #print(filename)
    #processedFiles(files)