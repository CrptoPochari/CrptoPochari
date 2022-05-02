import os  # operating system
products = []

#Part 1: Read Old csv
if os.path.isfile('products.csv'): # related path
	print("Yes, we have products.csv under this path.")
	#encoding="utf-8" could read the file.
	with open("products.csv", "r", encoding="utf-8") as file:
		for line in file:
			if "商品,價格" in line:
				continue
			#delete "\n", then split with ",""
			name, price = line.strip().split(",")
			products.append([name,price])
	print(products)
else:
	print("No, we dont' have products.csv under this path.")


#Part 2: Let user input
while True:
	name = input('Please enter product name:')
	
	#跳出: name= q不是商品
	if name == 'q':
		break
	price = int(input('Please enter product price:'))	
	
	#product.append(name)
	product = []
	products.append([name,price])

#Part 3: Print all purchase record
for product in products:
	print("Product: ",product[0],"'s Price= ", product[1])

#Part 4: Write the file
#it doesn't matter if we have products.csv, because we use write
#encoding ways is important
with open('products.csv', "w", encoding="utf-8") as f:
	f.write("商品,價格\n")
	for product in products:
		f.write(product[0] + ", " + str(product[1]) + "\n")