# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #we will use recursion
        #helper method with min and max params 
        #recursively pass in root.left and root.right with dfs. Use AND operatator to check left and right

        return self.inRange(float('-inf'), float('inf'), root)
    
    def inRange(self, minval, maxval, root) :
        if not root :
            return True
        if root.val <= minval or root.val >= maxval :
            return False
        
        return self.inRange(minval, root.val, root.left) and self.inRange(root.val, maxval, root.right)