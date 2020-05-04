# Build a tree for test
class Node:
	def __init__(self,data,left=None,right=None,parent=None):
		self.data=data
		self.left=left
		self.right=right
		self.parent=parent


tree=Node(0)
tree.left=Node(1)
tree.right=Node(2)
tree.left.left=Node(3)
tree.left.right=Node(4)

tree.left.parent=tree
tree.right.parent=tree
tree.left.left.parent=tree.left
tree.left.right.parent=tree.left
# First, ascend the deeper node to the same level as the other node.
# Then perform tandem upward movement of the two nodes. 
def lac(node_0,node_1):
	def get_depth(node):
		depth=0
		while node:
			depth+=1
			node=node.parent
		return depth

	depth_0,depth_1=get_depth(node_0),get_depth(node_1)
	# Make node_0 as the deeper node for simplifying the code.
	if depth_1>depth_0:
		node_0,node_1=node_1,node_0
	depth_diff=abs(depth_1-depth_0)
	# Ascend the deeper node to the same level as the other node.
	while depth_diff:
		node_0=node_0.parent
		depth_diff-=1
	# Ascend two nodes simultaneously.
	while node_0!=node_1:
		node_0,node_1=node_0.parent,node_1.parent
	return node_0
#Test
print(lac(tree.left.left,tree.left.right).data)
