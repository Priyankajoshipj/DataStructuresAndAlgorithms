# 24. Swap Nodes in Pairs
# given 1->2->3->4, you should return the list as 2->1->4->3.
# Given a linked list, swap every two adjacent nodes and return its head.

# You may not modify the values in the list's nodes, only nodes itself may be changed.
def swap_Nodes(head: ListNode) -> ListNode: #Iterative Approach [Accepted] beats -> 94.56% 
	prev = None
	curr = head

	while curr and curr.next:

		currNext = curr.next
		nextNext = currNext.next

		curr.next = nextNext
		currNext.next = curr

		if not prev:
			head = currNext
		else:
			prev.next = currNext
		prev = curr

		curr = nextNext

def swapPairs(head: ListNode) -> ListNode: #Recursive Approach [Accepted]
    if (not head or not head.next):
        return head
    second = head.next
    
    head.next = swapPairs(head.next.next)
    
    second.next=head
    
    return second