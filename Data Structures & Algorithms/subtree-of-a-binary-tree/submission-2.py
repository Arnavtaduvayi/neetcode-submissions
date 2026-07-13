# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root :
            return False 
        if not subRoot :
            return False

        if self.subtree(root, subRoot) :
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        

    def subtree (self, root, subroot) :
        if not root and not subroot:
            return True

        if root and subroot and root.val == subroot.val :
            return self.subtree(root.left, subroot.left) and self.subtree(root.right, subroot.right)

        else :
            return False

