# Tip: If the binary search doesn't find the exact number, the algorithm terminates and the square of l-1 is the closest number to k.  
def square_root(k):
	l,r=0,k
	while l<=r:
		m=l+(r-l)//2
		if m**2>k:
			r=m-1
		elif m**2==k:
			return m
		else:
			l=m+1
	return l-1
# Time complexity: O(logk), Space complexity: O(1)
# Test
print(square_root(16))
