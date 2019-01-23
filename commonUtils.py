#part of the SUSPL PHP framework
#to create a modal dialog box with bootstrap
#need to put select boxes and text boxes in a list and labels also will be in a sequence
#we need to mention how many selects and input boxes we are going to produce
#the select boxes will have only the default --select-- option added
#the remaining will need to be added manually


def doSelect(lblName, selName, f):
    f.write("<div class='row'>\n")
    f.write(getLabel(lblName,selName))
    f.write(getSelectBox(selName))
    f.write("</div>")
   
def doInput(lblName, inputName, f):
    f.write("<div class='row'>\n")
    f.write(getLabel(lblName,inputName))
    f.write(getInputBox(inputName, "Text"))
    f.write("</div>\n")

def doDate(lblName, dateName,f):
    #Date alone
    f.write("<div class='row'>\n")
    f.write(getLabel(lblName,dateName))
    f.write(getInputBox(dateName, "Date"))
    f.write("</div>\n")

def doSel2(lblName1, selName1, lblName2, selName2, f):   
    f.write("<div class='row'>\n")
    f.write(getLabel(lblName1,selName1))
    f.write(getSelectBox(selName1))
    f.write(getLabel(lblName2,selName2))
    f.write(getSelectBox(selName2))
    f.write("</div>") 

def doInput2(lblName1, inputName1, lblName2, inputName2, f):
    f.write("<div class='row'>\n")
    f.write(getLabel(lblName1,inputName1))
    f.write(getInputBox(inputName1, "Text")) 
    f.write(getLabel(lblName2,inputName2))
    f.write(getInputBox(inputName2, "Text"))
    f.write("</div>\n")

def doDate2(lblName1, dateName1, lblName2, dateName2,f):
    f.write("<div class='row'>\n")
    f.write(getLabel(lblName1,dateName1))
    f.write(getInputBox(dateName1, "Date")) 
    f.write(getLabel(lblName2,dateName2))
    f.write(getInputBox(dateName2, "Date"))
    f.write("</div>\n")

def doSelandInput(lblName1, selName, lblName2, inputName,inputType, f):
    # combo box and text box combo
    f.write("<div class='row'>\n")
    f.write(getLabel(lblName1, selName))
    f.write(getSelectBox(selName)) 
    f.write(getLabel(lblName2,inputName))
    f.write(getInputBox(inputName, inputType))
    f.write("</div>\n")

def doInputandSel(lblName1, inputName, lblName2, selName, inputType, f):
    # text box and combo box
    f.write("<div class='row'>\n")
    f.write(getLabel(lblName1,inputName))
    f.write(getInputBox(inputName, inputType))
    f.write(getLabel(lblName2, selName))
    f.write(getSelectBox(selName))
    f.write("</div>\n")

def doInput3(lblName1, inputName1, lblName2, inputName2, lblName3, inputName3, f):
    f.write("<div class='row mt-2'>\n")
    f.write("\t<label for='" + inputName1 + "' class='col-sm-1 col-form-label'>" + lblName1 + "</label>\n")
    f.write("\t<div class='col-sm-3'>\n")
    f.write("\t\t<input type='text' class='form-control' id='" + inputName1 + "' name='name'>\n")
    f.write("\t</div>\n")
    f.write("\t<label for='" + inputName2 + "' class='col-sm-1 col-form-label'>" + lblName2 + "</label>\n")
    f.write("\t<div class='col-sm-3'>\n")
    f.write("\t\t<input type='text' class='form-control' id='" + inputName2 + "' name='name'>\n")
    f.write("\t</div>\n")
    f.write("\t<label for='" + inputName3 + "' class='col-sm-1 col-form-label'>" + lblName3 + "</label>\n")
    f.write("\t<div class='col-sm-3'>\n")
    f.write("\t\t<input type='text' class='form-control' id='" + inputName3 + "' name='name'>\n")
    f.write("\t</div>\n")
    f.write("</div>\n")

def getLabel(lblName, selName):
    tmpstr = (f"\t<label for='{selName}' class='col-sm-2 col-form-label'>"
    f"{lblName}</label>\n")
    return tmpstr

def getSelectBox(selName):
    tmpstr = ("\t<div class='col-sm-4 dropdown'>\n"    +             
    "\t\t<select id='" + selName + "' class='form-control'>\n" +
    "\t\t\t<option disabled selected value=""> -- select -- </option>\n" +
    "\t\t</select>\n\t</div>\n")
    return tmpstr

def getInputBox(inputName, inputType):
    temstr = ("\t<div class='col-sm-4'>\n"
     "\t\t<input type='" + inputType +"' class='form-control' id='" + inputName + "' name='" + inputName + "'>\n" 
    "\t</div>\n")
    return temstr