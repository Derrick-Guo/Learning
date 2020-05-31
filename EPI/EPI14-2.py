# Build a BST class and instantiate a tree object.
class BST:
	def __init__(self,data=None,left=None,right=None):
		self.data,self.left,self.right=data,left,right

bst=BST(19,BST(7),BST(43))
bst.left.left,bst.left.right=BST(3),BST(11)
bst.right.left,bst.right.right=BST(23),BST(47)
bst.right.left.right=BST(37,BST(29,None,BST(31)),BST(41))

# Main function
def find_first_greater_than_k(tree,k):
	best_candidate=None
	while tree:
		if tree.data>k:
			best_candidate=tree.data 
			tree=tree.left
		else:
			tree=tree.right
	return best_candidate 
	# Time complexity: O(h), where h is the height of the BST. Space complexity: O(1).

print(find_first_greater_than_k(bst,23))