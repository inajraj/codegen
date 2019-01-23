import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

from commonUtils import doSelect, doInput, doDate, doInputandSel

f= open("test.php","w")

#doSelect("Bus Number", "selBN", f)
#doInput("Name", "txtName",f)
#doDate("Input Date", "dtInputDate", f)
doInputandSel("Bus Number", "txtBN", "Department", "selDept","Text",f)

f.close()