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

