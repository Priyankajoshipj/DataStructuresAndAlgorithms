# we don't want any instace of duplicate values 
# Input: 1->2->3->3->4->4->5
# Output: 1->2->5


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def remove_duplicates(head):

	if not head:
		return head

	prev = None
	curr = head

	while curr:
		repeat = False
		while curr.next and curr.val == curr.next.val:
			curr.next = curr.next.next
			repeat = True
		if repeat:
			if not prev:
				head = curr.next
			else:
				prev.next = curr.next
		else:
			if not prev:
				head = curr
				prev = head
			else:
				prev = curr
		curr = curr.next
	return head