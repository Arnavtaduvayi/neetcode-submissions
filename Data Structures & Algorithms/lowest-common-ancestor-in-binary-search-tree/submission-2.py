# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #property of a BST 
        #We have 2 possibilities: both p and q are going left or both going right. In this case, 
        #wherever they split is the LCA
        # However, if we hit either p or q BEFORE that, then whatever we hit has to be the LCA. 

        curr = root

        while curr :
            if curr.val == p.val :
                return p
            elif curr.val == q.val :
                return q
            if p.val < curr.val and q.val < curr.val :
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val :
                curr = curr.right 
            elif p.val < curr.val and q.val > curr.val or (p.val > curr.val and q.val < curr.val) :
                return curr
            
