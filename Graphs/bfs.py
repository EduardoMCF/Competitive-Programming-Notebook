def BFS(v):
	from collection import deque

	queue = deque()
	queue.append(v)
	seen[v] = 1
	parent[v] = -1
	while queue:
		v = queue.popleft()
		for neighbor in graph[v]:
			if not seen[neighbor]:
				queue.append(neighbor)
				distance[neighbor] = distance[v] + 1
				parent[neighbor] = v
				seen[neighbor] = 1

def shortestPath(start,end):
	'''Only works with unweighted Graphs'''
	BFS(v)
	if not seen[end]:
		return []

	path = []
	node = end
	while parent[node] != -1
		path.append(node)
		node = parent[node]
	path.append(node)
	return path[::-1]


n = int(input()) # Number of vertices
seen = [0]*n # Seen array
graph = [[] for i in range(n)] #Graph as adjacency list
distance,parent = [0]*n,[0]*n
