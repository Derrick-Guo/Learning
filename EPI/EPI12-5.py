import collections
# When we meet the word for the first time, we store the word itself as a key in a hash table, 
# and the index of the word as value. Update the nearest distance every time when we meet the same word again.
def find_nearest_repetition(paragraph):
	word_to_latest_index={}
	nearest_distance_so_far=float('inf')
	for i,word in enumerate(paragraph):
		if word in word_to_latest_index:
			nearest_distance_so_far=min(nearest_distance_so_far,i-word_to_latest_index[word])
		word_to_latest_index[word]=i
	
	return nearest_distance_so_far


# Test
paragraph=['All','work','and','no','and','work']
print(find_nearest_repetition(paragraph))
