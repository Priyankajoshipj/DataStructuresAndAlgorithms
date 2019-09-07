'''
given string of angle brackests.
Write a function that adds brackets to the beginning and end to make all angle brackets match.

'''
def balanceParenthesis(s):
	balance = 0
	ans = ''
	for p in s:
		if p == '>': 
			if balance == 0:
				ans = '<' + ans
				ans += p
			else:
				balance -= 1
				ans += p
		else:
			ans += p
			balance += 1
	while balance != 0:
		balance -= 1
		ans += '>'
	return ans


print(balanceParenthesis('><<><'))
# Output: '<><<><>>'