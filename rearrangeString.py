# 358. Rearrange String k Distance Apart HARD [Leetcode Premium]
from collections import Counter, deque
from heapq import heappop, heappush, heapify
def rearrangeString(s, k):
	count = Counter(s)
	res = ""
	heap = [(-v, key) for key, v in count.items()]
	heapify(heap)
	queue = deque()
	# max heap created 
	while heap:
		v, c = heappop(heap)
		res += c
		queue.append((v + 1, c))

		if len(queue) >= k:
			countval, char = queue.popleft()
			if countval < 0:
				heappush(heap, (countval, char))

	return res if len(res) == len(s) else ""

print("aaadbbcc: 2", rearrangeString("aaadbbcc", 2))
print("aaabc : 3", rearrangeString("aaabc", 3))
print("aabbcc : 2", rearrangeString("aabbcc", 2))