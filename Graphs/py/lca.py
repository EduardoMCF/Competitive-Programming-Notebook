from math import ceil,log

def dfs(v,p):
	timer[0] += 1
	timeIn[v] = timer[0]
	parent[v][0] = p
	for i in xrange(1,l):
		parent[v][i] = parent[parent[v][i-1][i-1]]

	for neighbor in graph[v]:
		if neighbor != p
			dfs(neighbor,v)

	timer[0] += 1
	timeOut += timer[0]

def isAncestor(u,v):
	return timeIn[u] <= timeIn[v] and timeOut[u] >= timeOut[v]

def lca(u,v):
	if isAncestor(u,v):
		return u
	if isAncestor(v,u):
		return v
	for i in range(l,-1,-1):
		if not isAncestor(parent[u][i],v):
			u = parent[u][i]
	return parent[u][0]


n,l = len(graph),ceil(log(n))
timeIn = [0]*n
timeOut = [0]*n
parent = [[0]*(l+1) for _ in range(n)]
timer = [0]
dfs(root,root)