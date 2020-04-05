from pandas import *
import re

from spellchecker import SpellChecker 

# spell = SpellChecker() 

# # find those words that may be misspelled 
# misspelled = spell.unknown(["ppressors", "recompese", "study"]) 

# for word in misspelled: 
# 	# Get the one `most likely` answer 
# 	print(spell.correction(word)) 

# 	# Get a list of `likely` options 
# 	print(spell.candidates(word)) 



def loadDictionary():
    xls = ExcelFile('C:/Users/User1/Downloads/WordCorrectionsDictionary.xlsx')
    df = xls.parse(xls.sheet_names[0])
    return df

def replaceWordsDummy(sentence):
    stuple = {"herlit" : "her/it","him lit" : "him/it", "youlthey":"you/they"}
    dest = "her/it"
    #sentence = 'lets call herlit great meeting'
    for x,y in stuple.items():
        sentence  = re.sub(rf"\b{x}\b", y, sentence)
    return sentence

def replaceWords(sentence, df):
                                
    

    # using a itertuples()  
    for keyval in df.itertuples(): 
        sentence  = re.sub(rf"\b{keyval[1]}\b", keyval[2], sentence)
        
    return sentence

    
#print(myxlobject)    
# 

def replace(match):
    return replacements[match.group(0)]
    

print(replaceWordsDummy('dfsdfs'))



#fileLines = ['Te thé quick', 'we show our deference te that', 'te whem makes such homage. Tiwards thi ladies']

# replacements = {'te':'to', 
#                 'thi':'the',
#                 'Te':'To',
#                'Thi':'The'}


# for sentence in fileLines:
#     print (re.sub('|'.join(r'\b%s\b' % re.escape(s) for s in replacements), 
#         replace, sentence) )
           
# notice that the 'this' in 'thistle' is not matched 
