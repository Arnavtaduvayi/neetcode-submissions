# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Maybe DFS, and on the way add checks to make sure all BST reqs are met for the given node

        return self.validate(root, float('-inf'), float('inf'))

    def validate(self, root, min_val, max_val):    
        if not root :
            return True
        
        if not (min_val < root.val < max_val) :
            return False
        
        return self.validate(root.left, min_val, root.val) and self.validate(root.right, root.val, max_val)

