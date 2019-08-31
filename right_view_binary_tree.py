# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def right_view(root):
    
    stack = [(root, 0)]
    rightmost_node = {}
    max_depth = -1
    while stack:
        popped, depth = stack.pop()
        rightmost_node.setdefault(depth, popped.val)
        max_depth = max(max_depth, depth)
        stack.append((popped.left, depth+1))
        stack.append((popped.right, depth+1))


    return [rightmost_node[i] for i in range(max_depth+1)]