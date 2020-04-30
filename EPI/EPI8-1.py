"""Implement a stack with max function, which returns the max value of its elements."""
class Stack:
	class MaxWithCount:
		def __init__(self,max,count):
			self.max,self.count=max,count

	def __init__(self):
		self._element=[]
		self._cached_max_with_count=[]

	def is_empty(self):
		return len(self._element)==0
	
	def max(self):
		if self.is_empty():
			raise IndexError('max():empty stack')
		return self._cached_max_with_count[-1].max

	def pop(self):
		if self.is_empty():
			raise IndexError('max():empty stack')
		poped_element=self._element.pop()
		current_max=self._cached_max_with_count[-1].max
		if current_max==poped_element:
			self._cached_max_with_count[-1].count-=1
			if self._cached_max_with_count[-1].count==0:
				self._cached_max_with_count.pop()
		return poped_element

	def push(self,x):
		self._element.append(x)
		if len(self._cached_max_with_count)==0:
			self._cached_max_with_count.append(self.MaxWithCount(x,1))
		else:
			current_max=self._cached_max_with_count[-1].max
			if x==current_max:
				self._cached_max_with_count[-1].count+=1
			elif x>current_max:
				self._cached_max_with_count.append(self.MaxWithCount(x,1))

# Test
stack=Stack()
stack.push(1)
stack.push(2)
stack.push(2)
stack.push(1)
stack.push(3)
stack.push(5)
print(stack.max())
print(stack.pop())
print(stack.max())

