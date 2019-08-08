# Reverse a singly linked list, both [Accepted] #Leetcode - 206
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode        """
        # my first attempt solution
        if not head:
            return None
        prev=head
        nextnode=head.next
        head.next=None
        if(not nextnode):
            return head
        while(nextnode):
            node1=nextnode.next
            nextnode.next=prev
            if(node1!=None):
                temp=node1.next
                node1.next=nextnode
                nextnode=temp
            else:
                node1=nextnode
                nextnode=None
            prev=node1      
                
        return node1
    # more straigh forward solution

    def reverseLinkedList(self, head):
        if not head:
            return None
        prev = None
        nodeN = head
        while (nodeN):
            nextNode = nodeN.next
            nodeN.next = prev
            prev = nodeN
            nodeN = nextNode