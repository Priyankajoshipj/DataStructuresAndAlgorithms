from collections import deque
def vertical_level_traversal(root):
    #Write your code here
    if not root:
        return None

    maps = {}

    queue = deque()
    horizontal_distance = 0
    queue.append((horizontal_distance, root))

    while queue:

        hd, node = queue.popleft()
        if not node:
            continue
        if hd not in maps:
            maps[hd] = [node.info]
        else:
            maps[hd].append(node.info) # for vertical level traversal
        
        queue.append((hd - 1, node.left))
        queue.append((hd + 1, node.right))
    for (key, value) in sorted(maps.items()):
        for j in value:
            print(j, end = " ")
    return 
        
