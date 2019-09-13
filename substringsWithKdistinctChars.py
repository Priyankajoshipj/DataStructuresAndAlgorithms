# Count substrings with exactly K distinct chars

def countSubstrings(s, k):
	n = len(s)
	chars = list(s)
	left, right = 0, 0
	sets = {}
	count = 0
	while right <= n:

		if len(sets) == k:
			print(sets, left, right)
			count += 1
			right += 1
		elif len(sets) > k:
			sets[chars[left]] -= 1
			if sets[chars[left]] == 0:
				del sets[chars[left]]
			left += 1
		else:
			if right < n:
				if chars[right] not in sets:
					sets[chars[right]] = 1
				else:
					sets[chars[right]] += 1
			right += 1
	return count 

print(countSubstrings("pqpqs",2))