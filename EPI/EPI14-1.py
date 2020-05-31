# Build a BST class and instantiate a tree object.
class BST:
	def __init__(self,data=None,left=None,right=None):
		self.data,self.left,self.right=data,left,right

bst=BST(19,BST(7),BST(43))
bst.left.left,bst.left.right=BST(3),BST(11)
bst.right.left,bst.right.right=BST(23),BST(47)

# Main function
def is_binary_tree_bst(tree,low_range=float('-inf'),high_range=float('inf')):
	if not tree:
		return True
	elif not low_range<=tree.data<=high_range:
		return False
	return is_binary_tree_bst(tree.left,low_range,tree.data) and is_binary_tree_bst(tree.right,tree.data,high_range)

# Test
print(is_binary_tree_bst(bst))