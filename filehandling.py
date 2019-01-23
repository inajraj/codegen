
#we need to mention how many selects and input boxes we are going to produce
#the select boxes will have only the default --select-- option added
#the remaining will need to be added manually

selectBoxes = ['selectMDType']
inputBoxes = ['inputValue']



f= open("guru99.txt","a+")

f.write("<div id='myModal' class='modal fade' role='dialog'>\n")
f.write("<div class='modal-dialog'>\n")
f.write("<!-- Modal content-->\n")
f.write("<div class='modal-content'>\n")
f.write("<div class='modal-header'>\n")
f.write("<button type='button' class='close' data-dismiss='modal'>&times;</button>\n")
f.write("<h4 class='modal-title' id='headerId' data-rowid='0'></h4>\n")
f.write(" </div>\n")
f.write("<div class='row mt-2'><div class='col-sm-1'></div>\n")
            <label for="inputBP" class="col-sm-3 col-form-label">Expense Type</label>
            <div class="col-sm-5">
            <select id="selectET"  class="form-control">
                <option disabled selected value=""> -- select -- </option>
                <?php include 'PopulateExpenseTypes.php';?>
            </select>
            </div>
        </div>
     

f.close()