import heapq
def merge_sorted_arrays(sorted_arrays):
	min_heap=[]
	# Build a list of iterators for arrays in sorted_arrays.
	sorted_arrays_iters=[iter(x) for x in sorted_arrays]
	# Put first elements from each iterator in min_heap.
	for i,it in enumerate(sorted_arrays_iters):
		first_element=next(it,None)
		if first_element is not None: # When comparing to None, it is better to use 'is' and 'is not', rather than '==' and '!='.
			heapq.heappush(min_heap,(first_element,i))

	result=[]
	while min_heap:
		smallest_element,smallest_array_i=heapq.heappop(min_heap)
		smallest_array_iter=sorted_arrays_iters[smallest_array_i]
		result.append(smallest_element)
		next_element=next(smallest_array_iter,None)
		if next_element is not None:
			heapq.heappush(min_heap,(next_element,smallest_array_i))
	return result
# Test
l1=[3,5,7]
l2=[0,6]
l3=[0,6,28]
sorted_arrays=[l1,l2,l3]
print(merge_sorted_arrays(sorted_arrays))