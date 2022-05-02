import os  # operating system


# Create function and make "products.csv" to argument
#Part 1: Read Old csv
def read_old(filename,products):
	#encoding="utf-8" could read the file.
	with open(filename, "r", encoding="utf-8") as file:
			for line in file:
				if "商品,價格" in line:
					continue
				#delete "\n", then split with ",""
				name, price = line.strip().split(",")
				products.append([name,price])
	return products

def user_input(products):
	#Part 2: Let user input
	while True:
		name = input('Please enter product name:')
		
		#跳出: name= q不是商品
		if name == 'q':
			break
		price = int(input('Please enter product price:'))	
		
		#product.append(name)
		products.append([name,price])
	return products

def print_all(products):
	#Part 3: Print all purchase record
	for product in products:
		print("Product: ",product[0],"'s Price= ", product[1])
	return products

def write_file(filename, products):
	print(products)
	#Part 4: Write the file
	#it doesn't matter if we have products.csv, because we use write
	#encoding ways is important
	with open(filename, "w", encoding="utf-8") as f:
		f.write("商品,價格\n")
		for product in products:
			f.write(product[0] + ", " + str(product[1]) + "\n")
	return products

# function core: do one thing!
# Thing do once? no function
def main():
	products = []
	filename = 'products.csv'
	if os.path.isfile(filename): # related path
		print("Yes, we have products.csv under this path.")		
		products = read_old(filename,products)
		print(products)
	else:
		print("No, we dont' have products.csv under this path.")
	products = user_input(products)
	products = print_all(products)
	products = write_file(filename, products)

#refactor
main()