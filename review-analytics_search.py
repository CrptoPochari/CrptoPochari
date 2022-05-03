import time
import progressbar


def Open_files(filename):
	#.ProgressBar() is not function, is a type of object! (self define)
	bar = progressbar.ProgressBar(max_value=1000000)
	#Open files + print len + remainder filter
	datas = []
	cnt = 0
	with open(filename,"r") as f:
		for line in f:
			datas.append(line)
			cnt += 1
			bar.update(cnt)
	return datas


def word_cnt(datas):
	start_time = time.time()	
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
	end_time = time.time()	
	print("It spend: ", end_time - start_time, " seconds.")
	
	return word_cnt

def search(word_cnt):	
	while True:
		word = input("what did you want to find?")
		if word == "q":
			break

		if word in word_cnt:
			print(word, "exist time= ", word_cnt[word])
		else:
			print("Not exist!")

	print("Thanks for using our searching system")

def main():
	datas = Open_files("reviews.txt")
	Worddic = word_cnt(datas)
	search(Worddic)

main()