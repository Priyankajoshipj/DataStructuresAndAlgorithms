# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters (premium)
'''
Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.

Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.
'''
def longestSubstring(s: str, k:int) -> int:
	if not s or k == 0:
        return 0
    if len(s) == 1:
        return 1
	lenls = 0
	maps = {}
	left = 0
	i = 0
	while left < len(s):
		print(i, lenls)
		ls = i - left
		while len(maps) <= k and i < len(s):
			if s[i] not in maps:
				maps[s[i]] = 1
			else:
				maps[s[i]] += 1
			ls += 1
			i += 1
		
		lenls = max(lenls, ls - 1)
		if len(maps) == k + 1:
			j = left
			while j < i + ls and len(maps) > k:
				maps[s[j]] -= 1
				ls -= 1
				left += 1
				if maps[s[j]] == 0:
					del maps[s[j]]
					left -= 1
				j += 1
		left += 1
	return lenls
print(longestSubstring("cbadabbcdef", 3))
