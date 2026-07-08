# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Maybe DFS, and on the way add checks to make sure all BST reqs are met for the given node

        #call a helper where we can track the real bounds for each node using parameters
        return self.validate(root, float('-inf'), float('inf'))

    def validate(self, root, min_val, max_val):    
        #base case, if root is None, its a valid BST. 
        if not root :
            return True
        
        #if our root value doesnt fall between the specified bounds, then it isnt valid BST
        if not (min_val < root.val < max_val) :
            return False
        
        #update min/max. If we go left, the MOST the next node can be is node.val - continue doing this all the way through
        return self.validate(root.left, min_val, root.val) and self.validate(root.right, root.val, max_val)

