# Input "226" o/p -> 3 explanation 2,26; 2,2,6 and 22,6
# 				226 Rec
# 			26(num) 		+ 6(num)
# 				2 				1 -> 3
def decode_ways(s): #Time Limit Exceeded in Leetcode for recursion, try DP
	def decode_rec(s):
        if len(s)<1:
            return 1
        if len(s) == 1:
            return 1
        if int(s[0]) == 0:
            return 0
        if (len(s) >= 2 and int(s[:2]) <= 26):
            return (decode_rec(s[1:]) + decode_rec(s[2:]))
        else:
            return decode_rec(s[1:])
    return decode_rec(s)


def decode_ways_dp(s): #Leetcode Accepted
    arr = {}
    if len(s)<1:
        return 0
    def decode_rec_dp(s,arr):
        if s in arr.keys():
            return arr[s]
        if len(s)<1:
            return 1
        if int(s[0]) == 0:
            return 0
        if len(s) == 1 :
            return 1
        if (len(s) >= 2 and int(s[:2]) <= 26 ):
            arr[s] = decode_rec_dp(s[1:],arr) + decode_rec_dp(s[2:],arr)
        else:
            arr[s] = decode_rec_dp(s[1:],arr)
        return arr[s]
    arr[s] = decode_rec_dp(s,arr)
    return arr[s]