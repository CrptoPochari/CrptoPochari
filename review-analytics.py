datas = [] 
count = 0
new = []
good =[]
#Open files + print len + remainder filter
with open("reviews.txt","r") as f:
	for line in f:
		datas.append(line)
#3. Message < 100 filter
		if len(line) < 100:
			new.append(line)
#4. Message have good
		if "good" in line:
			good.append(line)
#		count += 1
#		if count % 10000 ==0:
#			print(len(datas))

#Avg Length
sun_len = 0
for data in datas:
	sun_len += len(data)
print("Average= ", sun_len/len(datas), " Characters each.")
#3. Message < 100 filter
print("There are ", len(new), " message length< 100.")
#4. Message have good
print("There are ", len(good), " Message have good.")
