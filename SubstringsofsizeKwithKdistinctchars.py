
'''
Amazon interview question
Given a string s and an int k, return all unique substrings of s of size k with k distinct characters.

Example 1:

Input: s = "abcabc", k = 3
Output: ["abc", "bca", "cab"]
Example 2:

Input: s = "abacab", k = 3
Output: ["bac", "cab"]
Example 3:

Input: s = "awaglknagawunagwkwagl", k = 4
Output: ["wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag"]
Explanation: 
Substrings in order are: "wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag", "wagl" 
"wagl" is repeated twice, but is included in the output once.
Constraints:

The input string consists of only lowercase English letters [a-z]
0 ≤ k ≤ 26
'''
def SubstringK(s, k):
	n = len(s)
	chars = list(s)
	left, right = 0, 0
	sets = {}
	out = []
	while right <= n:
		size = right - left
		if len(sets) == k:
			out.append("".join(chars[left:right]))
			sets[chars[left]] -= 1
			if sets[chars[left]] == 0:
				del sets[chars[left]]
			left += 1
		elif size == k:
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
	return out 

print(SubstringK("awaglknagawunagwkwagl",4))


print(SubstringK("abacab",3))