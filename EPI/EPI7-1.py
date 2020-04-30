class ListNode:
	def __init__(self,data=0,next_node=None):
		self.data=data
		self.next=next_node
# Build two linked-list
l1=ListNode(2)
l1.next=ListNode(5)
l1.next.next=ListNode(7)

l2=ListNode(3)
l2.next=ListNode(11)
# Aimed function
def merge_two_sorted_lists(l1,l2):
	# Set dummy head and tail
	dummy_head=tail=ListNode()
	# Set the position for the head
	if l1.data>l2.data:
		dummy_head.next=l2
	else:
		dummy_head.next=l1
	
	while l1 and l2:
		if l1.data<l2.data:
			tail.next,l1=l1,l1.next
		else:
			tail.next,l2=l2,l2.next
		tail=tail.next
	
	tail.next=l1 or l2
	return dummy_head.next
# Test 
merged_list=merge_two_sorted_lists(l1,l2)
while merged_list:
	print(merged_list.data)
	merged_list=merged_list.next