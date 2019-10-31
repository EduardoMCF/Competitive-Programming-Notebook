class Edge:
	def __init__(self,v = -1,w = float('inf')):
		self.v = v
		self.w = w

	def check(self):
		return self.w == float('inf')

def prim(graph):
	n,totalWeight = len(graph),0
	seen = [0]*n
	minEdge = [Edge()]*n

	minEdge[0].w = 0
	for i in range(n):
		v = -1
		for j in range(n):
			if not seen[j] and (v == -1 or minEdge[j].w < minEdge[v].w):
				v = j

		if minEdge[v].check():
			return -1

		seen[v] = 1
		totalWeight += minEdge[v].w
		if minEdge[v].v != 1:
			path.append((v,minEdge[v].v))

		for to in xrange(n):
			if graph[v][to] < minEdge[to].w:
				minEdge[to] = (graph[v][to],v)
	
	return minEdge,totalWeight

