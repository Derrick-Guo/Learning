# Tip: Since insert an element into an array is expensive, write from the end.
def merge_two_sorted_arrays(A,m,B,n):
	a,b,write_idx=m-1,n-1,m+n-1
	while a>=0 and b>=0:
		if A[a]>B[b]:
			A[write_idx]=A[a]
			a-=1
		else:
			A[write_idx]=B[b]
			b-=1
		write_idx-=1
	while b>=0:
		A[write_idx]=B[b]
		write_idx,b=write_idx-1,b-1
# Time complexity: O(m+n). Space complexity: O(1)
# Test
A=[5,13,17,None,None,None,None,None]
B=[3,7,11,19]
merge_two_sorted_arrays(A,3,B,4)
print(A)