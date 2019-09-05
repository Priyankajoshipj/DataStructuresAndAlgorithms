def allPossibleCombination(s):

	n = len(s)
	if n <2:
		return n

	out = set()

	def rec_comb_helper(s, i, out):
		if i == len(s) - 1:
			return ["", s[i]]
		one = rec_comb_helper(s, i+1, out)
		for com in one:
			if s[i] not in com:
				com1 = s[i] + com 
				out.add(com1)
			out.add(com)
		return list(out)
	allp = rec_comb_helper(s, 0, out)
	print(sorted(allp))

	def permute(choices, s, out1):
		if not s:
			return [""]
		if len(choices) == len(s):
			string = "".join(choices)
			out1.append(string)
		for i in range(len(s)):
			choice = s[i]
			if choice in choices:
				continue
			choices.append(choice)
			permute(choices, s, out1)
			choices.pop()
		return out1
	res = []
	for comb in allp:
		a = permute([], comb, [])
		res += a
	print(sorted(res))
	return res
allPossibleCombination("ABC")