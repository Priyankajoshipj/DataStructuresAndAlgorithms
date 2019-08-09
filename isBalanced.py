# Leetcode 110 [Accepted]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
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
        
        def isbal(root):
            if not root or (not root.right and not root.left):
                return True
            elif root.right and root.left:
                rightdep = findDepth(root.right)
                leftdep = findDepth(root.left)
                if abs(rightdep - leftdep) > 1:
                    return False
                else:
                    return isbal(root.right) and isbal(root.left)
            elif root.right:
                if findDepth(root.right) > 1:
                    return False
                else:
                    return isbal(root.right)
            elif root.left:
                if findDepth(root.left) > 1:
                    return False
                else:
                    return isbal(root.left)
        return isbal(root)