class Solution:
	def setKthBit(self, n, k):
	    m=1<<k
	    return (n | m)
	