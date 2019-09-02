class Node:
    def __init__(self, value):
        self.val = value
        self.next = None
class Queue:
	def __init__(self):
		self.front = None
		self.tail = None

	def push(self, value: int) -> None:
		new = Node(value)
		if not self.tail:
			self.tail = new
		else:
			self.tail.next = new
			self.tail = new
		if not self.front:
			self.front = new
		return None

    def pop(self) -> int:
        popped = self.front.val if self.front else None
        self.front = self.front.next if self.front else None

        return popped

	def top(self) -> int:
		return self.front.val

	def empty(self) -> None:
		return not self.front and not self.tail


