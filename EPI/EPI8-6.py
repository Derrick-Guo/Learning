# Build a tree
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
tree.right.left=Node(5)
tree.right.right=Node(6)

# Main function
def binary_tree_depth_order(tree):
	result=[]
	if not tree:
		return result

	curr_depth_nodes=[tree]
	while curr_depth_nodes:
		result.append([curr.data for curr in curr_depth_nodes])
		curr_depth_nodes=[
			child
			for curr in curr_depth_nodes for child in (curr.left,curr.right)
			if child
		]
	return result
# Test
res=binary_tree_depth_order(tree)
print(res)