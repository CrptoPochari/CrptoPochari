import random

r = random.randint(1,100)
count = 0
while True:
	count += 1
	print("This is ", count ,"Times you guest.")
	entnum = int(input("Enter your number: "))
	if entnum == r:	
		print("Correct\n")
		break
	elif entnum < r:
		print("Wrong, bigger please.\n")
	else:
		print("Wrong, smaller please.\n")