
//general fuction to check a name contains invalid characters
//controlName is the actual control name in the screen
//FieldName is what we ll display 
//blankFlag is if the field can have blank or not 
function checkName(controlName, FieldName, blankFlag) {
	if (blankFlag != 'Y')  {
		if ( $('#'+controlName).val() == '') {
			bootbox.alert(FieldName + ' can not be blank'); 
			return false;
		}
	}
	if( /^[a-zA-Z0-9- ]*$/.test( $('#'+controlName).val() ) == false ) {
		bootbox.alert(FieldName + ': input is not alphanumeric');
		return false;
	}
	return true;
}

//the function is to convert the date string provided by datepicker to the format
//which is mentioned in the parameter
//the separator is also mentioned like - or / 
function GetFormattedDate(val, formatStr,separatorStr) {
    console.log(val);
    if (val == null) {
        return "";
    }
    var tdate = new Date(val);
    var month = tdate.getMonth() + 1;
    var day = tdate.getDate();
    var year = tdate.getFullYear();
    if (formatStr == "mdy")
        return month + separatorStr + day + separatorStr + year;
    if (formatStr == "dmy")
        return day + separatorStr + month + separatorStr + year;
    if (formatStr == "ymd")
        return year + separatorStr + month + separatorStr + day;
    if (formatStr == "ydm")
        return year + separatorStr + day + separatorStr + month;
        
}