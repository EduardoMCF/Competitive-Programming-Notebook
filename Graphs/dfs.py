def DFS(v):
	seen[v] = 1
	for neighbor in graph[v]:
		if not seen[neighbor]:
			dfs(neighbor)

def DFS_Iterative(v):
	from collections import deque

	stack = deque()
	stack.appendleft(v)
	while stack:
		v = stack.popleft()
		for neighbor in graph[v]:
			if not seen[neighbor]:
				stack.appendleft(neighbor)
				seen[neighbor] = 1


n = int(input()) # Number of vertices
seen = [0]*n # Seen array
graph = [[] for i in range(n)] #Graph as adjacency list
