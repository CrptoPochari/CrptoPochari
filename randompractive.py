import random

r = random.randint(1,100)
while True:
	entnum = int(input("Enter your number: "))
	if entnum == r:	
		print("Correct")
		break
	elif entnum < r:
		print("Wrong, bigger please.")
	else:
		print("Wrong, smaller please.")