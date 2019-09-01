# implement queue with stacks
class Node:
    def __init__(self, value):
        self.val = value
        self.next = None
class stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new = Node(value)
        new.next = self.head
        self.head = new

    def pop(self):
        if not self.head:
            return None
        nex = self.head.next
        popped = self.head
        self.head = nex
        return popped.val if popped else None

    def empty(self):
        return not self.head

    def peek(self):
        return self.head.val if self.head else None


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = stack()
        self.stack2 = stack()
        self.front = None

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if self.stack2.empty():
            if self.stack1.empty():
                self.front = x
            self.stack1.push(x)	
        else:
            while not self.stack2.empty():
                self.stack1.push(self.stack2.pop())

            self.stack1.push(x)

        return None 
        
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        while not self.stack1.empty():
            n = self.stack1.pop()
            self.stack2.push(n)
        
        popped = self.stack2.pop()
        self.front = self.stack2.peek()
        return popped


    def peek(self) -> int:
        """
        Get the front element.
        """        
        return self.front
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        
        return self.stack1.empty() and self.stack2.empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()