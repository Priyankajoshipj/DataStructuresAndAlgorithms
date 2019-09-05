from collections import Counter
def find_max_len(words, letters):
	letterCount = Counter(letters)
	maxl = float('-inf')
	for word in words:
		if len(word) > maxl:
			lc = letterCount
			isword = True
			for c in word:
				if c in lc:
					lc[c] -= 1
				else:
					isword = False
					break
			if isword:
				maxl = len(word)

	return maxl

words = [ "og", "cat", "good"]
letters = ['o', 'g', 'd', 'c', 'a', 't', 'o']
print("Input: ", words, letters)
print("Output: ",find_max_len(words, letters))