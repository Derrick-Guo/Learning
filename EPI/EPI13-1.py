# Brute-force method: Take a time complexity of O(mn), where m and n are the length of array A and B.
def intersect_two_sorted_arrays(A,B):
	return [a for i,a in enumerate(A) if (a in B) and (i==0 or a!=A[i-1])]

# A better method is to iterate through the first array and use binary search to see whether the element is in the second array.
# This method takes a time complexity of O(mlogn),where m is the length of A and n is the length of B.
import bisect
def intersect_two_sorted_arrays(A,B):
	def is_present(k):
		i= bisect.bisect_left(B,k)
		return i<len(B) and B[i]==k
	return [a for i,a in enumerate(A) if is_present(a) and (i==0 or a!=A[i-1])]

# When A and B have similar length, there's another method faster than methods above.
# This method takes a time complexity of O(m+n), where m and n are the length of the two arrays.
def intersect_two_sorted_arrays(A,B):
	i,j,intersection=0,0,[]
	while i<len(A) and j<len(B):
		if A[i]==B[j]:
			if i==0 or A[i-1]!=A[i]:
				intersection.append(A[i])
			i,j=i+1,j+1
		elif A[i]>B[j]:
			j+=1
		else:
			i+=1
	return intersection
#  Test
a=[2,3,4]
b=[1,3,5]
print(intersect_two_sorted_arrays(a,b))