datas = [] 
count = 0

#Open files + print len + remainder filter
with open("reviews.txt","r") as f:
	for line in f:
		datas.append(line)
		count += 1
		if count % 10000 ==0:
			print(len(datas))

#Avg Length
sun_len = 0
for data in datas:
	sun_len += len(data)
print("Average= ", sun_len/len(datas), " Characters each.")