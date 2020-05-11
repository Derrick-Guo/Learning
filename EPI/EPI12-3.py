import collections
class LRUCache:
	def __init__(self,capacity):
		self._isbn_price_table=collections.OrderedDict()
		self._capacity=capacity

	def lookup(self,isbn):
		if isbn not in self._isbn_price_table:
			return -1
		price=self._isbn_price_table.pop(isbn)
		self._isbn_price_table[isbn]=price
		return price

	def insert(self,isbn,price):
		# In the specification, if ISBN is already present, insert should not change the price,
		# but it should update that entry to be the most recently used entry.
		if isbn in self._isbn_price_table:
			price=self._isbn_price_table.pop(isbn)
		elif self._capacity<=len(self._isbn_price_table):
			self._isbn_price_table.popitem(last=False) 
			# The popitem() method for ordered dictionaries returns and removes a (key, value) pair. 
			# The pairs are returned in LIFO order if last is true or FIFO order if false. 
		self._isbn_price_table[isbn]=price
# Time complexity: Lookup takes O(1), and updating the queue takes O(1).
# Test:
lrucache=LRUCache(2)
lrucache.insert(1,100)
lrucache.insert(2,200)
print(lrucache.lookup(2))
lrucache.insert(3,300)
print(lrucache.lookup(1))