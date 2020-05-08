import heapq
class star:
	def __init__(self,name,distance):
		self.name=name
		self.distance=distance

a=star('a',1)
b=star('b',2)
c=star('c',3)
stars=[a,b,c]

# Main function
def find_closest_k_stars(stars,k):
	max_heap=[]
	for star in stars:
		heapq.heappush(max_heap,(-star.distance,star.name))
		if len(max_heap)>k:
			heapq.heappop(max_heap)
	return [s[1] for s in heapq.nlargest(k,max_heap)]

# Test
print(find_closest_k_stars(stars,2))


