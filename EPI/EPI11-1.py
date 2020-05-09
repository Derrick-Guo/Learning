# Tip: Record the current occurance, and update this variable once another occurance is found later.
def search_first_of_k(A,k):
	l,r=0,len(A)-1
	first_occurance=-1
	while l<=r:
		m=l+(r-l)//2
		if A[m]>k:
			r=m-1
		elif A[m]<k:
			l=m+1
		else:
			first_occurance=m # Key point, see the tip
			r=m-1
	return first_occurance
# Test
a=[1,2,2,3,3,3]
print(search_first_of_k(a,3))

