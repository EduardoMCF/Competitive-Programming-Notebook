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

#parent can be an array or a dictonary