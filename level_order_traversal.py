# Easy DFS Iterative Solution 
# 102. Binary Tree Level Order Traversal
def levelOrder(self, root: TreeNode) -> List[List[int]]:
    levelmap={}
    output = []
    if not root:
        return []
    def dfs(root):
        if not root:
            return
        dfsstack=[]
        dfsstack.append((root,1))
        while(dfsstack):
            node,level=dfsstack.pop()
            if level not in levelmap.keys():
                levelmap[level]=[node.val]
            else:
                levelmap[level].append(node.val)
            if node.right:
                dfsstack.append((node.right,level+1))
            if node.left:
                dfsstack.append((node.left,level+1))
        return
    dfs(root)
    for keys in levelmap.keys():
        output.append(levelmap[keys])
    return output