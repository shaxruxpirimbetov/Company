def check_phone(phone):
	# +998 90 123 45 67
	phone = phone.replace("+", "")
	symbols = [i for i in "0123456789"]
	if len(phone.replace("+", "")) != 12:
		return {"status": False, "message": "Invalid Len"}
	
	for i in phone:
		if i not in symbols:
			return {"status": False, "message": f"Invalid symbol '{i}'"}
	
	if phone[0:3] != "998":
		return {"status": False, "message": "Invalid country"}
	
	return {"status": True, "message": f"+{phone}"}

