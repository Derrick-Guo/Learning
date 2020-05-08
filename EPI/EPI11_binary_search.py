def bsearch(t,A):
	l,r=0,len(A)
	while l<=r:
		m=l+(r-l)//2
		if A[m]>t:
			r=m-1
		elif A[m]==t:
			return m
		else:
			l=m+1
	return False
# Test
A=[1,2,3,4,5,6,7,8]
print(bsearch(8,A))