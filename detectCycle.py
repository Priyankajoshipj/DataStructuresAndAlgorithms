#142. Linked List Cycle II [Accepted]
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        
        cyclicNode = self.cycle(head)
        
        pointer1 = head
        pointer2 = cyclicNode
        if cyclicNode is None:
            return None
        while pointer1 != pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        return pointer1
        
    def cycle(self,head):
        slow =head
        fast= head
        
        while(fast!=None and fast.next!=None):
            fast=fast.next.next
            slow=slow.next
            if(fast ==slow):
                return slow
        return None