def dijkstra(start,n):
	inf = float('inf')
	distance = [inf]*n
	parent = [-1]*n
	seen = [0]*n

	distance[start] = 0
	for i in range(n):
		v = -1
		for j in range(n):
			if not seen[j] and (v == -1 or distance[j] < distance[v]):
				v = j

		if distance[v] == inf:	break

		seen[v] = 1
		for neighbor,weight in graph[v]:
			if distance[v] + weight < distance[neighbor]:
				distance[neighbor] = distance[v] + weight
				parent[neighbor] = v

	return distance,parent,seen

def getShortestPath(start,end,n):
	parent = dijkstra(start,n)[1]

	path = []
	node = end
	while parent[node] != -1:
		path.append(node)
		node = parent[node]
	path.append(node)
	return path[::-1]

def sparseDijkstra(start,n):
	from heapq import heappush as push, heappop as pop
	inf = float('inf')
	distance = [inf]*n
	parent = [-1]*n
	PQueue = []

	distance[start] = 0
	push(PQueue,(0,start))
	while PQueue:
		weight,v = pop(PQueue)

		if weight != distance[v]: continue

		for neighbor,weightN in graph[v]:
			if distance[v] + weightN < distance[neighbor]:
				distance[neighbor] = distance[v] + weightN
				parent[neighbor] = v
				push(PQueue,(distance[neighbor],neighbor))

	return distance,parent