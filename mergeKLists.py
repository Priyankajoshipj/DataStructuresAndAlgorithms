class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

def mergeTwoLists(node1: Node, node2: Node) -> Node:
	newNode = Node(0)
	newhead = newNode
	while node1 and node2:
		if node1.val < node2.val:
			newNode.next = node1
			node1 = node1.next
		else:
			newNode.next = node2
			node2 = node2.next
		newNode = newNode.next

	if node2:
		newNode.next = node2
	else:
		newNode.next = node1
	return newhead.next


def mergeKLists( lists: List[ListNode]) -> ListNode:
	if not lists:
		return lists

	l = len(lists)
	i = 1
	while i < l:
		for j in range(0, n-i, i * 2)
			lists[j] = mergeTwoLists(lists[j], lists[i + j])
		i *= 2

	return lists[0]

	 