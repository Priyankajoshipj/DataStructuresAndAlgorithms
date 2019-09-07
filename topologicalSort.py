'''
given a graph
{
	0: []
	1: [0]
	2: [0]
	3: [1, 2]
	4: [3]
}
output : [0, 1, 2, 3, 4]
'''
def topologicalSort(graph):
	visited = set()
	visiting = set()
	out = []
	def dfs(node):
		if node in visited:
			return
		if node in visiting:
			print(node)
			raise NameError("Can't do a topologicalSort since graph has a cycle")

		neighbors = graph[node]
		visiting.add(node)
		for n in neighbors:
			
			if n not in visited:
				dfs(n)
		visiting.remove(node)
			
		visited.add(node)
		out.append(node)

	for k in graph.keys():
		dfs(k)

	return out

g = {
	0: [],
	1: [4],
	2: [0],
	3: [2],
	4: [1]
}

print(topologicalSort(g))
#Output : [0, 2, 3, 4, 1]