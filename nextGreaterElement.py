class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        max2 = float('-inf')
        n2 = len(nums2)
        n1 = len(nums1)
        stack = []
        maps = {}
        for i in range(n2):
            if not stack:
                stack.append(nums2[i])
            if nums2[i] < stack[-1]:
                stack.append(nums2[i])
            while(stack and stack[-1] < nums2[i]):
                n = stack.pop()
                maps[n] = nums2[i]
            stack.append(nums2[i])
        while stack:
            n = stack.pop()
            maps[n] = -1
        res = []
        for j in range(n1):
            res.append(maps[nums1[j]])
        return res
            