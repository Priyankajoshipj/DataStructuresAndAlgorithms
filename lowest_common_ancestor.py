# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 236. Lowest Common Ancestor of a Binary Tree space and time comp : O(n)
class Solution: #[Accepted]
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        node = root
        ans = None
        def rec(node, ans):
            curr = False
            if not node:
                return False, ans
            left, ans =rec(node.left, ans)
            right, ans = rec(node.right, ans)
            if node.val ==p.val or node.val == q.val:
                curr = True
            if curr + left + right >= 2:
                ans = node
            return (curr or left or right, ans)
        
        l, ans = rec(root, ans)
        return ans