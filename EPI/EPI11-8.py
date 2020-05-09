import random
def find_kth_largest(k,A):
	def partition_around_pivot(l,r,p):
		# This function is to partition the array around pivot, and returns the new index of the pivot.
		# After partitioning, the elements on the left side of pivot are greater than pivot,
		# and the elements on the right side are smaller than pivot. 
		p_val=A[p] # Save the value of pivot for subcequent comparision.  
		new_p=l # Set new_pivot pointer to the leftmost. 
		A[r],A[p]=A[p],A[r] # Switch the value of pivot to the rightmost of the array.
		for i in range(l,r):  # Except the rightmost value reserved earlier, compare each value to pivit value.
			if A[i]>p_val: # If the ith value is greater than pivot value, switch it to the new pivot position.
				A[i],A[new_p]=A[new_p],A[i]
				new_p+=1 # Once the switch is done, move new pivot pointer to the right by 1.
		A[r],A[new_p]=A[new_p],A[r] # After all the comparision, switch the pivot value to the new pivot pointer position.
		return new_p
	l,r=0,len(A)-1
	while l<=r:
		p=random.randint(l,r) # Generate a random integer in [l,r], which r is included.
		new_p=partition_around_pivot(l,r,p) 
		if new_p==k-1:
			return A[new_p]
		elif new_p>k-1:
			r=new_p-1
		else:
			l=new_p+1
# Test
a=[0,1,3,2,4,5]
print(find_kth_largest(4,a))

