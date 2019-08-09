# 104. Maximum Depth of Binary Tree LeetCode [Accepted]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def maxDepth(root: TreeNode) -> int:
	
	def findDepth(root):
		if not root:
			return 0

		if not root.right and not root.left:
			return 1
		elif root.right and root.left:
			return max(findDepth(root.right),findDepth(root.left)) + 1
		elif root.right:
			return findDepth(root.right) + 1
		else:
			return findDepth(root.left) + 1 

	return findDepth(root)



