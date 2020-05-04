# Build a tree for test
class Node:
	def __init__(self,data,left=None,right=None):
		self.data=data
		self.left=left
		self.right=right

tree=Node(0)
tree.left=Node(1)
tree.right=Node(2)
tree.left.left=Node(3)
tree.left.right=Node(4)
tree.left.left.left=Node(5)
tree.left.left.right=Node(6)

# When checking a subtree, all we need to know is whether it is balanced, and if so, what its height is.
# To do this, we use namedtuple to create a container which contains imformation of 'balanced' and 'height'.
import collections
def is_balanced_binary_tree(tree):
	BalancedStatusWithHeight=collections.namedtuple('BalancedStatusWithHeight',('balanced','height'))
	def check_balanced(tree):
		if not tree:
			return BalancedStatusWithHeight(True,-1)  # Base case.

		# Check its left subtree.	
		left_result=check_balanced(tree.left)
		if not left_result.balanced:
			return BalancedStatusWithHeight(False,0)
		# Check its right subtree.
		right_result=check_balanced(tree.right)
		if not right_result.balanced:
			return BalancedStatusWithHeight(False,0)
		# If its left and right subtree are balanced, calculate if itself is balanced, and its height.
		is_balanced=abs(left_result.height-right_result.height)<=1
		height=max(left_result.height,right_result.height)+1
		return BalancedStatusWithHeight(is_balanced,height)

	return check_balanced(tree).balanced

# Test
print(is_balanced_binary_tree(tree))
