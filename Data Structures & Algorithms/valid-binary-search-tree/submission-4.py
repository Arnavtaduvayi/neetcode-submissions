# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #Make a new function with new mins and maxes as params so that we know which range each number HAS to fall into 

        return self.isvalid(root, float('-inf'), float('inf'))


    def isvalid(self, root, minv, maxv) :
        # Every time we go to a new node, say we go left, we have to update the max param to be whatever
        # the curr value was since we know an upper bound. 
        if not root :
            return True

        if root.val > minv and root.val < maxv :
            return self.isvalid(root.left, minv, root.val) and self.isvalid(root.right, root.val, maxv)
        else :
            return False