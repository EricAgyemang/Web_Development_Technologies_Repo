function formValidate()
{
	var userId = document.registration.userid;
        //try var uid = document.getElementsByName("userid")[0];
        var errorMessage ="";	 	
	let idValidation = idValidate(userId,5,12);

        if (idValidation&& passwordValidation&& zipValidate)
	     return true;
	else
	     return false;	
}	



function idValidate(userId,mi,mx)
{
	var userId_len = userId.value.length;
	
	if (userId_len == 0 || userId_len <= mi || userId_len > mx)
	{
		errorMessage = "User id should not be empty or the length should be between "+mi+" to "+mx;
		alert(errorMessage);
		userId.focus();
		return false;
	}
	return true;

}

var userPassword = document.registration.userpassword;

let passwordValidation = passwordValidate(userPassword,7,12);


function passwordValidate(userPassword,mx,my)
{
	var password_len = userPassword.value.length;
	if (password_len == 0 ||password_len >= my || password_len < mx)
	{
		errorMessage +="<br>" + "Password should not be empty  or the length should be between "+mx+" to "+my;
		document.getElementById("error").innerHTML=errorMessage;
                alert(errorMessage);
		userPassword.focus();
		return false;
	}
	return true;
}


var userZip = document.registration.zip;

Let zipValidation = zipValidate (userZip);

function zipValidate(userZip)
{ 
	var numbers = /^[0-9]+$/;
	if(userZip.value.match(numbers))
	{
		return true;
	}
	else
	{
		alert('ZIP code must have numeric characters only');
		userZip.focus();
		return false;
	}
}

