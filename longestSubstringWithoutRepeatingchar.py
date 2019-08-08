#Longest substring withour repeating characters 
'''
s = 'pwwkew'
i = 0, j = 0, res = 0, arr = ()
pass1 : add p to set, increment j => i = 0, j = 1, res = max(0, 1 - 0), arr(p)
pass2 : add w to set, increment j => i = 0, j = 2, res = max(1, 2 - 0), arr(p, w)
pass3 : w is in arr, remove p (ith char) increment i =>  i = 1, j = 2, res = max(2, 2 - 1), arr(w)
pass4 : w is in arr, remove w increment i =>  i = 2, j = 2, res = max(2, 2 - 2), arr()
pass5 : w not in arr add to set, increment j => i = 2, j = 3, res = max(2, 3 - 2), arr(w)
pass6 : k not in arr add to set, increment j => i = 2, j = 4, res = max(2, 4 - 2), arr(w, k)
pass7 : e not in arr add to set, increment j => i = 2, j = 5, res = max(2, 5 - 2), arr(w, k, e)
pass8 : w in arr remove w (ith char) increment i => i = 3, j = 4, res = max(3, 4 - 3), arr(k, e)
pass9 : w not in arr add to set, increment j => i = 3, j = 6, res = max(3, 6 - 3), arr(k, e, w)
j > n : break return 3
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        i=0
        j=0
        res=0
        arr=set()
        while(i<n and j<n):
            if(s[j] not in arr):
                arr.add(s[j])
                j+=1
                res=max(res,j-i)
            else:
                arr.remove(s[i])
                i+=1
        return res