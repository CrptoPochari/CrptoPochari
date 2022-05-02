
data = []
#with open架構會自動關閉，此處再#8關閉
with open("food.txt", "r") as f:
	for line in f:
		#data.append(line)  # with open read 會出現換行符號
		data.append(line.strip()) #檔案讀取常用

#print(data)