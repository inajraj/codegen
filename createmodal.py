#part of the SUSPL PHP framework
#to create a modal dialog box with bootstrap
#need to put select boxes and text boxes in a list and labels also will be in a sequence
#we need to mention how many selects and input boxes we are going to produce
#the select boxes will have only the default --select-- option added
#the remaining will need to be added manually

import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

from commonUtils import doSelect
from commonUtils import doInput, doInput2


userInputs = [('selectMDType','Master Data Type'), ('inputValue','Value'), ('inputName', "Driver1")]

f= open("guru99.php","a+")

f.write("<div id='myModal' class='modal fade' role='dialog'>\n")
f.write("<div class='modal-dialog'>\n")
f.write("<!-- Modal content-->\n")
f.write("<div class='modal-content'>\n")
f.write("<div class='modal-header'>\n")
f.write("<button type='button' class='close' data-dismiss='modal'>&times;</button>\n")
f.write("<h4 class='modal-title' id='headerId' data-rowid='0'></h4>\n")
f.write(" </div>\n")

for x in userInputs:
    res = x[0].find("select")
    if (res > -1):
        doSelect(x[1],x[0],f)
        continue
    res = x[0].find("input")
    if (res > -1):
        doInput(x[1],x[0],f)

doInput2("lblDate","inputDate","lblBN", "inputBN",f)
f.write("</div>\n</div>\n")
f.close()

