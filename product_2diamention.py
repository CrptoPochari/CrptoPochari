products = []
while True:
	name = input('Please enter product name:')
	
	#跳出: name= q不是商品
	if name == 'q':
		break
	price = input('Please enter product price:')	
	
	#product.append(name)
	product = []
	"""
	#1
	#	product.append(name)
	#	product.append(price)
	#2
	#	product = [name,price]
	#	products.append(product)
	"""
#3
	products.append([name,price])

for product in products:
	print("Product: ",product[0],"'s Price= ", product[1])