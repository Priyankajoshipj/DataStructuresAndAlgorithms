#Hackerrank challenge
from collections import deque
def topView(root):
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
        # if hd not in maps:
        #     maps[hd] = node.val
        # else:
        #     maps[hd].append(node.val) # for vertical level traversal
        if hd not in maps:
            maps[hd] = node.info
        queue.append((hd - 1, node.left))
        queue.append((hd + 1, node.right))
    for (key, value) in sorted(maps.items()):
        print(value, end = " ")
    return 