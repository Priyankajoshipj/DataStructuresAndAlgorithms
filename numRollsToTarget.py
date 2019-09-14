'''
You have d dice, and each die has f faces numbered 1, 2, ..., f.

Return the number of possible ways (out of fd total ways) modulo 10^9 + 7 to roll the dice so the sum of the face up numbers equals target.

 

Example 1:

Input: d = 1, f = 6, target = 3
Output: 1
Explanation: 
You throw one die with 6 faces.  There is only one way to get a sum of 3.
Example 2:

Input: d = 2, f = 6, target = 7
Output: 6
Explanation: 
You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7:
1+6, 2+5, 3+4, 4+3, 5+2, 6+1.

1155. Number of Dice Rolls With Target Sum
'''
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if target == 1 and d > 1:
            return 0
        
        dp = {}
        def recdp(d, f, target):
            if (d,target) in dp:
                return dp[(d, target)]
            if target == 0:
                return 1 if d == 0 else 0
            ways = 0
            if d > 0:            
                for i in range(1, f+1):
                    if target - i > -1:
                        ways += recdp(d-1, f, target - i)
                dp[(d, target)] = ways
            return ways
        
       
        numberOfWays = recdp(d, f, target)
        
        return numberOfWays % (1000000007)