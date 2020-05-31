# Build a BST class and instantiate a tree object.
class BST:
	def __init__(self,data=None,left=None,right=None):
		self.data,self.left,self.right=data,left,right

bst=BST(19,BST(7),BST(43))
bst.left.left,bst.left.right=BST(3),BST(11)
bst.right.left,bst.right.right=BST(23),BST(47)
bst.right.left.right=BST(37,BST(29,None,BST(31)),BST(41))

# Main function
def find_k_largest_in_bst(tree,k):
	def find_k_largest_in_bst_helper(tree):
		if tree and len(k_largest_elements)<k:
			find_k_largest_in_bst_helper(tree.right)
			if len(k_largest_elements)<k:
				k_largest_elements.append(tree.data)
				find_k_largest_in_bst_helper(tree.left)

	k_largest_elements=[]
	find_k_largest_in_bst_helper(tree)
	return k_largest_elements
# Time complexity: O(h+k). Since we descends in the tree at most h, so we plus h. Space complexity: O(1).
# Test
print(find_k_largest_in_bst(bst,4))

