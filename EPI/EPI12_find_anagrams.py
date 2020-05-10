# Tip: add sorted version for each string in the strings as keys, 
# and store corresponding original strings as values.
import collections
def find_anagrams(strings):
	# Build a dictionary of which the values are lists.
	sorted_string_to_anagrams=collections.defaultdict(list)
	for s in strings:
		sorted_string_to_anagrams[''.join(sorted(s))].append(s)
	return [group for group in sorted_string_to_anagrams.values() if len(group)>=2]

# Time complexity: The computation consists of n sorts and n insertions into the hash table. 
# Sorting the keys has time complexity O(nmlogm), for m is the length of the longest string.
# Insertions add a time complexity of O(nm), yielding O(nmlogm) time complexity in total.

# Test
strings=['elvis','lives','levis','money','silent','listen']
print(find_anagrams(strings))
