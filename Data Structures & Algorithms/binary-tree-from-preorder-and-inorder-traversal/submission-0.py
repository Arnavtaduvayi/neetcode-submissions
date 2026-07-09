# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #first in preorder HAS to be root. 
        #in an inorder list, the root has the left values on the left of it and hte right values on the right of it 
        #so, just find the root in the inorder and call that mid. Now, the first on each side (left,right)
        #of the root will be the roots to the next thing. Just recursively repeat this for the right and left sde
        #we need to get the mid index for the inorder list, and then we can just do [1 : mid+1] for the preorder, left
        # and [0 :  mid] for the inorder since we just need the left side. 

        if not preorder or not inorder :
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[0 : mid])
        root.right = self.buildTree(preorder[mid + 1 : len(preorder)], inorder[mid + 1 : len(preorder)])

        return root
