def trapping_rain_water(height):
	#2 pass approach - Dynamic Programming Time and space complexity O(n)
	if not height:
		return 0
	n = len(height)
	max_left = [0 for i in range(n)]
	max_right = [0 for i in range(n)]
	max_right[0] = height[0]
	max_right[n-1] = height[n-1]
	area = 0
	for i in range(n):
		max_left[i] = max(height[i], max_left[i-1])

	for i in range(n-1):
		max_right[n-i-1] = max(height[i], max_right[n-i])

	for i in range(n):
		area += min(max_left[i], max_right[i]) - height[i]

	return area

#approach 2: Two pointer solution time O(n), space O(1)
def trapping_rain_water(height):
	if not height:
        return 0
    n = len(height)

    max_right = float('-inf')
    max_left = float('-inf')
    left = 0
    right = n-1
    ans = 0
    while(left < right):
        if height[left] < height[right]:
            if max_left >= height[left]:
                ans += max_left - height[left]
            else:
                max_left = height[left]

            left += 1
        else:
            if max_right >= height[right]:
                ans += max_right - height[right]
            else:
                max_right = height[right]
            right -= 1
    return ans