# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #first in pre is always the root. In the inorder, the left of the pre root is the left subtrees, 
        #and the right is the right subtrees
        if not preorder or not inorder :
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[0 : mid])
        root.right = self.buildTree(preorder[mid + 1 : len(preorder)], inorder[mid + 1 : len(preorder)])


        return root