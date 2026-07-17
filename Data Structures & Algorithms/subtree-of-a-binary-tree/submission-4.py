# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # make a recursive function that just goes through all kids and checks if they are
        # the same, then base -> returns true if None; same, false if not? 

        if not root :
            return False
        if not subRoot :
            return False

        if self.recur(root, subRoot) :
            return True
        else :
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def recur(self, root, subRoot) :
        if not root and not subRoot : 
            return True
        if root and subRoot and (root.val != subRoot.val):
            return False
            
        if root and subRoot :
            return self.recur(root.left, subRoot.left) and self.recur(root.right, subRoot.right)
        else :
            return False