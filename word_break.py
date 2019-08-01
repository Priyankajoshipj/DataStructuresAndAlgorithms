# Word break, LeetCode problem #139
# s = "goalspecial" 
# wordDict = ["go", "goal", "goal", "special"]

# helper_rec(0,1) -> helper_rec(1,2) or helper_rec(0,2)
# 					False				(4,5) or (0,5)
# 										True	False
# TRY Dynamic Programming
def word_break(s, wordDict): #Time limit exceeded, Leetcode
	if not s:
            return true
        if s in wordDict:
            return True
    def helper_rec(s, wordDict, left, right):
        n = len(s)
        if right >= n:
            return False
        if (left > right):
            return True
        if not s:
            return True

        if s[right:n] in wordDict and s[left:right] in wordDict:
            return True
        if s[left:right] in wordDict:
            return helper_rec(s,wordDict, right, right+1) or helper_rec(s,wordDict, left, right+1)
        else:
            return helper_rec(s,wordDict, left, right+1)
    return helper_rec(s,wordDict, 0, 1)

#Modified from the above recursive approach
#Accepted in Leetcode
#Can be optimized
 def word_break_DP(s, wordDict): 
 	wordDict = set(wordDict)
 	if not s:
            return true
    if s in wordDict:
        return True
    def helper_dp(s, wordDict, left, right, s_array):
        n = len(s)
        if right >= n:
            return False
        if (left > right):
            return True
        if not s:
            return True
		if s[right:n] in wordDict and s[left:right] in wordDict:
            return True
        
        if (left, right) in s_array.keys():
        	return s_array[(left, right)]
        if s[left:right] in wordDict:
            s_array[(left, right)] = helper_dp(s,wordDict, right, right+1, s_array) or helper_dp(s,wordDict, left, right+1, s_array)
        else:
            s_array[(left, right)] =  helper_dp(s,wordDict, left, right+1, , s_array)
        return s_array[(left, right)]
    return helper_dp(s,wordDict, 0, 1, {})

#Optimized DP
# [Accepted]
def word_break_DP_optimized(s, wordDict):
	wordDict = set(wordDict)
 	if not s:
            return true
    if s in wordDict:
        return True
    n = len(s)
    s_array = [False] * (n+1)
    s_array[0] = True
    for i in range(n+1):
    	if s[:i] in wordDict:
    		s_array[i] = True
    		continue
	    for j in range(1,i):
	    	if s_array[j]:
	    		if s[j:i] in wordDict:
	    			s_array[i] = True
	    			break
    return s_array[-1]