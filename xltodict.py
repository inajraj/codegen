from pandas import *
import re

def replaceWords(fileLines):
                                 
    xls = ExcelFile('C:/Users/User1/Downloads/WordCorrectionsDictionary.xlsx')
    df = xls.parse(xls.sheet_names[0])

    # using a itertuples()  
    for keyval in df.itertuples(): 
       #search and replace keyval 1 with keyval 2
       src = " " + keyval[1] + " "
       dest = " " + keyval[2] + " "
       for sentence in fileLines:
           sentence  = re.sub(r"\bte\b", 'to', sentence)
           print(sentence)


    print(fileLines)
#print(myxlobject)    
# 

def replace(match):
    return replacements[match.group(0)]
    
fileLines = ['Te thé quick', 'we show our deference te that', 'te whem makes such homage. Tiwards thi ladies']

replacements = {'te':'to', 
                'thi':'the',
                'Te':'To',
                'Thi':'The'}


for sentence in fileLines:
    print (re.sub('|'.join(r'\b%s\b' % re.escape(s) for s in replacements), 
        replace, sentence) )
           
# notice that the 'this' in 'thistle' is not matched 
