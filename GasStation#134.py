#Greedy algorith approach - Not very optimal for this example
# Time Complexity worst case O(n^2), average case: O(nlogn)
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        m = []
        if n ==0 :
            return 0
        if n == 1:
            return 0 if gas[0]>=cost[0] else -1
        for i in range(n):
            x = (gas[i]/cost[i],i) if cost[i]!= 0 else (gas[i], i)
            m.append(x)

        m.sort(reverse = True)
        def can_run_clockwise(start,cost,gas):
            i = start
            gas_remaining =0
            steps = 0
            while steps<=len(gas):
                if gas_remaining < 0:
                    return False
                if i == start and steps != 0:
                    return True
                if i == len(gas):
                    i = 0

                gas_remaining += gas[i] - cost[i]

                i+=1
                steps+=1
            return True
        j = 0
        while j<len(m):
            start = m[j][1]
            if can_run_clockwise(start,cost,gas):
                return start
            else:
                j+=1
        return -1

#More optimal one pass solution
