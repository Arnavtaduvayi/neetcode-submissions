# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #   parent
        #    | 
        #   5 
        #  /    \
        #-10, right
        #leftgain = max(0, dfs(node.left))
        #if that subtree hurts us, pretend it contributes 0. 

        best = root.val


        def dfs(node) :

            if not node: 
                return 0
            
            leftGain = dfs(node.left)
            leftGain = max(0, leftGain)

            rightGain = dfs(node.right)
            rightGain = max(0, rightGain)

            currentPath = node.val + leftGain + rightGain 
            
            nonlocal best

            best = max(best, currentPath)

            return node.val + max(leftGain, rightGain)

        dfs(root)
        return best
            



