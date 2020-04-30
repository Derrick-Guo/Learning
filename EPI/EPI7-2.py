class ListNode:
	def __init__(self,data=0,next_node=None):
		self.data=data
		self.next=next_node
# Build two linked-list
l=ListNode()
l.next=ListNode(11)
l.next.next=ListNode(7)
l.next.next.next=ListNode(5)
l.next.next.next.next=ListNode(3)
l.next.next.next.next.next=ListNode(2)

# while l:
# 	print(l.data)
# 	l=l.next

# Main function
def reverse_sublist(l,start,finish):
	# initialize dummy head of the whole list and the head of sublist to be reversed
	dummy_head = sublist_head = ListNode(0,l)

	for _ in range(1,start):
		sublist_head=sublist_head.next

	sublist_iter=sublist_head.next
	for _ in range(finish-start):
		temp=sublist_iter.next
		sublist_head.next,temp.next,sublist_iter.next=temp,sublist_head.next,temp.next
		# sublist_iter.next,temp.next,sublist_head.next=temp.next,sublist_head.next,temp

	return dummy_head.next

# Test
reversed_sublist=reverse_sublist(l,3,5)
while reversed_sublist:
	print(reversed_sublist.data)
	reversed_sublist=reversed_sublist.next

