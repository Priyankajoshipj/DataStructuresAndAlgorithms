from collections import deque
def TreasureIsland(matrix):
	rows = len(matrix)
	cols = len(matrix[0])

	queue = deque()

	queue.append((0, 0, 0))

	neighbors = [(1, 0), (0, 1), (-1, 0), (0, -1)]
	seen = set()
	seen.add((0,0))
	while queue:
		r, c, level = queue.popleft()
		if matrix[r][c] == 'X':
			return level
		
		for n in neighbors:
			child_row = r + n[0]
			child_col = c + n[1]

			if child_col < cols and child_col > -1 and child_row < rows and child_row > -1 and (child_row, child_col) not in seen:
				if matrix[child_row][child_col] != 'D':
					queue.append((child_row, child_col, level+1))
					seen.add((child_row, child_col))
	return -1

Tmap = [['O', 'O', 'O', 'O'], ['D', 'O', 'D', 'O'], ['O', 'O', 'O', 'O'], ['X', 'D', 'D', 'O']]
treasure = TreasureIsland(Tmap)
print(treasure)