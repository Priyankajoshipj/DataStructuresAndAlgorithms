#LRU Cache implementation in Python
class Node:
    def __init__(self,  key: int,val: int):
        self.val=val
        self.prev=None
        self.next=None
        self.key=key
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.dictionary=dict()
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head
        
    def get(self, key: int) -> int:
        if(key in self.dictionary):
            node=self.dictionary[key]
            self.remove(node)
            self.add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if(key in self.dictionary):
            self.remove(self.dictionary[key])
        node=Node(key,value)
        self.add(node)
        self.dictionary[key]=node
        if(len( self.dictionary)>self.capacity):
            node=self.head.next
            
            self.remove(node)
            
            del self.dictionary[node.key]
                
    def remove(self, node):
        prev=node.prev
        next1=node.next
        prev.next=next1
        next1.prev=prev
        
    def add(self, node):
        prev=self.tail.prev
        prev.next=node
        self.tail.prev=node
        node.prev=prev
        node.next=self.tail

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)