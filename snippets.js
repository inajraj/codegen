

if (!checkName('txtFirstName', 'FirstName'))
	return false;

if (!checkName('MiddleName', 'MiddleName'))
	return false;

if (!checkName('LastName', 'LastName'))
	return false;

if (!checkName('FullName', 'FullName'))
	return false;

if (!checkName('FatherName', 'FatherName'))
	return false;

if (!checkName('SpouseName', 'SpouseName'))
	return false;

var dte = new Date($('DOB').val);
var minDate = new Date();
var maxDate = new Date();
minDate.setDate(minDate.getDate() - 0);
maxDate.setDate(maxDate.getDate() - 25550);
var res = validateDate(dte,minDate,maxDate)
if (res == -1) 
	bootbox.alert('DOB is lower than Minium Date allowed');
if (res == 1) 
	bootbox.alert('DOB is greater than Maximum Date allowed');

var dte = new Date($('JoiningDate').val);
var minDate = new Date();
var maxDate = new Date();
minDate.setDate(minDate.getDate() - 0);
maxDate.setDate(maxDate.getDate() - 10);
var res = validateDate(dte,minDate,maxDate)
if (res == -1) 
	bootbox.alert('Joining Date is lower than Minium Date allowed');
if (res == 1) 
	bootbox.alert('Joining Date is greater than Maximum Date allowed');

var regex=/^(\+\d{1,3}[- ]?)?\d{10}$/;
if (!$(MobileNo).val().match(regex)) 
	bootbox.alert('MobileNo is not a valid Mobile Number');

var dte = new Date($('LeavingDate').val);
var minDate = new Date();
var maxDate = new Date();
minDate.setDate(minDate.getDate() - 0);
maxDate.setDate(maxDate.getDate() - 0);
var res = validateDate(dte,minDate,maxDate)
if (res == -1) 
	bootbox.alert('Leaving Date is lower than Minium Date allowed');
if (res == 1) 
	bootbox.alert('Leaving Date is greater than Maximum Date allowed');

var dte = new Date($('ResignationDate').val);
var minDate = new Date();
var maxDate = new Date();
minDate.setDate(minDate.getDate() - 0);
maxDate.setDate(maxDate.getDate() - 10);
var res = validateDate(dte,minDate,maxDate)
if (res == -1) 
	bootbox.alert('Resignation Date is lower than Minium Date allowed');
if (res == 1) 
	bootbox.alert('Resignation Date is greater than Maximum Date allowed');

if (!$(LeavingDate).val() >=  $(ResignationDate).val())
	bootbox.alert('Leaving Date should be Greater than or equal to ResignationDate');

if ($(Active).val() == No && ($(LeavingDate).val() == null || $(LeavingDate).val()  ==''))
	bootbox.alert('Active should not be 'No' if LeavingDate is empty');

if ($(LeavingDate).val() != '' && ($(ResignationDate).val() == null || $(ResignationDate).val()  ==''))
	bootbox.alert('ResignationDate should not be blank if LeavingDate has value');

if (($(LastName).val() == null || $(LastName).val()  =='') && ($(Initials).val() == null || $(Initials).val()  ==''))
	bootbox.alert(' Either LastName or Initials should have value');

if (!checkName('txtFirstName', 'FirstName'))
	return false;

if (!checkName('MiddleName', 'MiddleName'))
	return false;

if (!checkName('LastName', 'LastName'))
	return false;

if (!checkName('FullName', 'FullName'))
	return false;

if (!checkName('FatherName', 'FatherName'))
	return false;

if (!checkName('SpouseName', 'SpouseName'))
	return false;

var dte = new Date($('DOB').val);
var minDate = new Date();
var maxDate = new Date();
minDate.setDate(minDate.getDate() - 0);
maxDate.setDate(maxDate.getDate() - 25550);
var res = validateDate(dte,minDate,maxDate)
if (res == -1) 
	bootbox.alert('DOB is lower than Minium Date allowed');
if (res == 1) 
	bootbox.alert('DOB is greater than Maximum Date allowed');

var dte = new Date($('JoiningDate').val);
var minDate = new Date();
var maxDate = new Date();
minDate.setDate(minDate.getDate() - 0);
maxDate.setDate(maxDate.getDate() - 10);
var res = validateDate(dte,minDate,maxDate)
if (res == -1) 
	bootbox.alert('Joining Date is lower than Minium Date allowed');
if (res == 1) 
	bootbox.alert('Joining Date is greater than Maximum Date allowed');

var regex=/^(\+\d{1,3}[- ]?)?\d{10}$/;
if (!$(MobileNo).val().match(regex)) 
	bootbox.alert('MobileNo is not a valid Mobile Number');

var dte = new Date($('LeavingDate').val);
var minDate = new Date();
var maxDate = new Date();
minDate.setDate(minDate.getDate() - 0);
maxDate.setDate(maxDate.getDate() - 0);
var res = validateDate(dte,minDate,maxDate)
if (res == -1) 
	bootbox.alert('Leaving Date is lower than Minium Date allowed');
if (res == 1) 
	bootbox.alert('Leaving Date is greater than Maximum Date allowed');

var dte = new Date($('ResignationDate').val);
var minDate = new Date();
var maxDate = new Date();
minDate.setDate(minDate.getDate() - 0);
maxDate.setDate(maxDate.getDate() - 10);
var res = validateDate(dte,minDate,maxDate)
if (res == -1) 
	bootbox.alert('Resignation Date is lower than Minium Date allowed');
if (res == 1) 
	bootbox.alert('Resignation Date is greater than Maximum Date allowed');

if (!$(LeavingDate).val() >=  $(ResignationDate).val())
	bootbox.alert('Leaving Date should be Greater than or equal to ResignationDate');

if ($(Active).val() == No && ($(LeavingDate).val() == null || $(LeavingDate).val()  ==''))
	bootbox.alert('Active should not be 'No' if LeavingDate is empty');

if ($(LeavingDate).val() != '' && ($(ResignationDate).val() == null || $(ResignationDate).val()  ==''))
	bootbox.alert('ResignationDate should not be blank if LeavingDate has value');

if (($(LastName).val() == null || $(LastName).val()  =='') && ($(Initials).val() == null || $(Initials).val()  ==''))
	bootbox.alert(' Either LastName or Initials should have value');