def numIslands(island: List[List[str]]) -> int:
	if not island:
		return 0
	R = len(island)
	C = len(island[0])

	if R == C == 1 :
		return 0 if island[0][0] == '0' else 1
	seen = set()
	neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]

	def dfs(x, y, island):
		seen.add((x, y))
		if island[x][y] == '0':
			return 
		for n in neighbors:
			r = x + n[0]
			c = y + n[1]
			if r > -1 and r < R and c > -1 and c < C and (r, c) not in seen:
				dfs(r, c, island)

		return
	count = 0
	for i in range(R):
		for j in range(C):
			if island[i][j] == '1' and (i,j) not in seen:
				dfs(i, j, island)
				count += 1
			else:
				if (i, j) not in seen:
					seen.add((i,j))
	return count






