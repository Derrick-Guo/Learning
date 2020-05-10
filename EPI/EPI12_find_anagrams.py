import collections
def find_anagrams(strings):
	# Build a dictionary of which the values are lists.
	sorted_string_to_anagrams=collections.defaultdict(list)
	for s in strings:
		sorted_string_to_anagrams[''.join(sorted(s))].append(s)
	return [group for group in sorted_string_to_anagrams.values() if len(group)>=2]

# Test
strings=['elvis','lives','levis','money','silent','listen']
print(find_anagrams(strings))