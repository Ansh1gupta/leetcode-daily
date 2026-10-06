class Solution:
	def binaryToDecimal(self, b):
		result=0
		pow=0
		m=int(b)
		while(m>0):
		    d=m%10
		    num=(2**pow)*d
		    result+=num
		    pow+=1
		    m=m//10
		return result
		    
		