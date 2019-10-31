class SparseTable:
	
	def __init__(self,array,func):
		self.array = array
		self.func = func
		self._log = self._logPreprocess()
		self.sparseTable = self._preprocess()

	def _logPreprocess(self):
		n = len(self.array);
		_log = [0] * (n+1)

		for i in range(2,n+1):
			_log[i] = _log[n//2] + 1

		return _log

	def _preprocess(self):
		n = len(self.array)
		k = self._log[n]+1
		sTable = [[0]*k for i in range(n)]

		for i in range(n):
			sTable[i][0] = self.array[i]
		
		for j in range(1,k+1):
			for i in range(n+1):
				if i + (1 << j) > n: break
				sTable[i][j] = self.func(sTable[i][j-1], sTable[i + (1 << (j-1))][j-1])

		return sTable

	def query(self,l,r):
		l,r = min(l,r),max(l,r)
		j = self._log[r-l+1]

		return self.func(self.sparseTable[l][j], self.sparseTable[r-(1 << j)+1][j])

	def __len__(self):
		return len(self.array)

	def __getitem__(self,interval):

		if type(interval) == int:
			if interval < 0: raise IndexError("Negatives indexes aren't supported")
			l,r = (interval,interval)
		else:
			l = interval.start or 0
			r = interval.stop or len(self.array)-1
			if l < 0 or r < 0: raise IndexError("Negatives indexes aren't supported") 

		return self.query(l,r)
		
	def __str__(self):
		return '\n'.join(' '.join(map(str,row)) for row in self.sparseTable)

	def __repr__(self):
		return f"SparseTable({self.array},{self.func.__name__})"
			
				
