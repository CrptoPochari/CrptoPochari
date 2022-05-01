#output = [(operation) for variable in list *condition]
good = []
datas = []
bads = []
with open("reviews.txt","r") as lines:
	datas = [line for line in lines]
print("datas have ",len(datas)," message")

good = [data for data in datas if "good" in data]
print("good have ",len(good)," message")

# boolean operation replace condition
bads = ["bad" in data for data in datas]
print("good have ", bads ," message")