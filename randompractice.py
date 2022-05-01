import random

start = 1
end = 1

# input option
while start >= end:
	print("Enter your range:")
	start = int(input("Start= "))
	end = int(input("End= "))
	print("Start should be smaller than End\n")

print("your Start=", start ,", End=", end ,".\n")
r = random.randint(start,end)

# Comparison and hint
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