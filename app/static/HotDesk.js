function verifyAddDeskForm()
	{
		if( document.confirmAddDesk.indate == "")
		{
			alert("Please provide a valid date for free seat !");
			document.confrimAddDesk.indate.focus() ;
			return false;
		}
		if( document.confirmAddDesk.infloor == "")
		{
			alert("Please provide a valid Floor for free seat !");
			document.confrimAddDesk.infloor.focus() ;
			return false;
		}
		if( document.confirmAddDesk.indeskno == "")
		{
			alert("Please provide a valid Desk# for free seat !");
			document.confrimAddDesk.indeskno.focus() ;
			return false;
		}
		return (true);
	}