#Remove duplicates from an array
#In-place solution space comp: O(1), time - O(n) worstcase : 2-pass solution when all the elements are equal
def Remove_duplicates(nums):
	lastDisctinct = 0
	n = len(nums)
	for i in range(n-1):
		if nums[i] != nums[i+1]:
			nums[i], nums[lastDisctinct] = nums[lastDisctinct], nums[i]
			lastDisctinct += 1

	nums[lastDisctinct] = nums[n-1]
	lastDisctinct += 1

	for k in range(lastDisctinct, n): #This step can be removed if we can slice the array but that will take extra space
		nums.pop()

	return nums

nums = [1, 2, 2, 3, 4, 4, 4, 5, 5] 

print(Remove_duplicates(nums))
# [1, 2, 3, 4, 5]

#  space O(n) soluction, Time O(n)
def remove_duplicates_from_unsorted_array(nums):
	setmap = set()
	out = []
	for i in range(len(nums)):
		if nums[i] not in setmap:
			out.append(nums[i])
			setmap.add(nums[i])

	return out

nums = [1, 2, 5, 1, 7, 2, 4, 2]

print(remove_duplicates_from_unsorted_array(nums)) # retaining the order in which it was entered
