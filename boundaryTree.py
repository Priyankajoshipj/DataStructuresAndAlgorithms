class Node: 
  
    # Constructor to create a new node 
    def __init__(self, data): 
        self.val = data  
        self.left = None
        self.right = None

def boundaryTree(root):
	
	out = []

	def leftBoundary(root, out):
		if root:
			if root.left:
				out.append(root.val)
				out = leftBoundary(root.left, out)
			elif root.right:
				out.append(root.val)
				out = leftBoundary(root.right, out)
		return out

	def leafBoundary(root, out):
		if root:
			out = leafBoundary(root.left, out)

			if not root.left and not root.right:
				out.append(root.val)
			out = leafBoundary(root.right, out)
		return out

	def rightBoundary(root, out):
		if root:
			if root.right:
				out = rightBoundary(root.right, out)
				out.append(root.val)
			elif root.left:
				out.append(root.val)
				out = rightBoundary(root.left, out)
		return out

	if root:
		out.append(root.val)

		out = leftBoundary(root.left, out)

		out = leafBoundary(root.left, out)
		out = leafBoundary(root.right, out)

		out = rightBoundary(root.right, out)

	return out

root = Node(20) 
root.left = Node(8) 
root.left.left = Node(4) 
root.left.right = Node(12) 
root.left.right.left = Node(10) 
root.left.right.right = Node(14) 
root.right = Node(22) 
root.right.right = Node(25) 

print(boundaryTree(root))

