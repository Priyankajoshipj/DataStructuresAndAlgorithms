class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        prevmap = {}
        maps = {}
        for i in range(n):

            if not stack:
                stack.append(i, nums[i])
            if nums[i] < stack[-1]:
            	stack.append(nums[i])
            while(stack and stack[-1] < nums[i]):
                n = stack.pop()
                maps[n] = nums[i]
            stack.append(nums[i])

        for i in range(n):
        	