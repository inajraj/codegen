import os.path
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

def createValidateDate(f):
    f.write("function validateDate(dt, mindate, maxdate) {")
    f.write("\n\tvar dte = new Date($(dt).val())")
    f.write("\n\tif (dte < minDate)")
    f.write("\n\t\talert('Date is older than limit');")
    f.write("\n\tif (dte > maxDate)")
    f.write("\n\t\talert('Date is newer than limit');")
    f.write("\n}")

f = open("snippets.js","a+")
createValidateDate(f)
f.close()



