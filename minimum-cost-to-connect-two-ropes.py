# https://leetcode.com/problems/minimum-cost-to-connect-sticks (premium)
from heapq import heappush, heappop
def min_cost_to_connect(ropes):
	if len(ropes) < 2:
		return 0
	heap = []
	for rope in ropes:
		heappush(heap, rope)

	def cal_cost(heap):
		total = 0
		while len(heap) > 1:
			min1 = heappop(heap)
			min2 = heappop(heap)
			minSum = min1 + min2
			total += minSum
			heappush(heap, minSum)
		return total

	return cal_cost(heap)

ropes = [8, 4, 6, 12]
print(min_cost_to_connect(ropes))
# 58
ropes = [20, 4, 8, 2]
print(min_cost_to_connect(ropes))
# 54
ropes = [1, 2, 5, 10, 35, 89]
print(min_cost_to_connect(ropes))
# 224
ropes = [2, 2, 3, 3]
print(min_cost_to_connect(ropes))
# 20