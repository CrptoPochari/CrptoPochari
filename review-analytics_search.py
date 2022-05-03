def Open_files(filename):
	#Open files + print len + remainder filter
	datas = [] 
	with open(filename,"r") as f:
		for line in f:
			datas.append(line)
	return datas


def word_cnt(datas):	
	word_cnt = {}
	# data = 1 review, datas = 100 millions review list
	for data in datas:
		# split() would be better than split(" ")
		words = data.split()
		for word in words:
			if word in word_cnt:
				word_cnt[word] += 1
			else:
				word_cnt[word] = 1 # add new key to wc dictionary

	for word in word_cnt:
		if word_cnt[word] > 10000000:
			print(word,": ", word_cnt[word])

	while True:
		word = input("what did you want to find?")
		if word == "q":
			break

		if word in word_cnt:
			print(word, "exist time= ", word_cnt[word])
		else:
			print("Not exist!")

	print("Thanks for using our search system")

def main():
	file = Open_files("reviews.txt")
	word_cnt(file)


main()