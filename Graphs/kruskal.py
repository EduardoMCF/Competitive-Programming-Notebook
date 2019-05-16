from random import sample



def makeSet(v):
	parent[v] = v

def find(v):
	path = []
	while parent[v] != v:
		path.append(v)
		v = parent[v]

	for node in path:
		parent[node] = v

	return v

def union(a,b):
	a,b = find(a),find(b)
	if a != b:
		a,b = sample([a,b])
		parent[b] = a

def kruskal(n,edges):
	'''
	O(mlogn)
	n = number of vertices
	edges array must be in ther form (v1,v2,weight)'''

	for i in range(n):
		makeSet(i)

	edges.sort(key = lambda x: x[-1])

	MST,totalWeight = [],0
	for v1,v2,weight in edges:
		if find(v1) != find(v2):
			totalWeight += weight
			MST.append((v1,v2,weight))
			union(v1,v2)

	return MST,totalWeight
