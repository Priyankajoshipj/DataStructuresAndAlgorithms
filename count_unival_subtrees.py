# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#unival tree is incremented if the root.val == root.left.val and root.val == root.right.val

#		0
#	1		0
#1		1		1
#			1		1  output - 6
def find_unival_tree(root):
	
	def count_unival(root, count):
		if not root:
			return count
		if not root.left and not root.right:
			return count+1
		if (((not root.left or root.left.val == root.val) and (not root.right or root.right.val == root.val))):
                return  count_unival(root.left,count) + count_unival(root.right,count) + 1
            if root.left and root.right:
                if (root.left.val == root.val and root.right.val == root.val):
                    return  count_unival(root.left,count) + count_unival(root.right,count) + 1
            return count_unival(root.left, count) + count_unival(root.right, count)
        return count_unival(root, 0)