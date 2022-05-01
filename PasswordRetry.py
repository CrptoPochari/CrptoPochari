password = "a123456"
count = 3
while True:	
	entpwd = input("Enter your password:")
	if count == 0:
		print("Failed 3 times, exit!")
		break
	elif entpwd == password:	
		print("Correct")
		break
	else:
		print("Wrong, ",count," times left.")
		count = count-1