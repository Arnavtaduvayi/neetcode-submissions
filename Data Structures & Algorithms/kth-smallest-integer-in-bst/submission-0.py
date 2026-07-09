# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #Go through the tree, add everything to a pq, pop however many times needed to get to the kth element
        #adding and popping from pq -> O(logn), traversing tree -> O(n) || pq -> O(n) space -- conditions are met. 

        #go to the very left, and now you have a min value. To find the k smallest, you can climb back up to the right, 
        #k times. Once you cant climb back up to the right, you can start going right. 

        #in order traversal -> make an array, go to kth index -> kaboom

        #in order: 
        #left, .val, right


        res = []
        self.makeList(root, res)
        return res[k - 1]


    def makeList(self, root: Optional[TreeNode], res) :
        if not root :
            return
        
        self.makeList(root.left, res)
        res.append(root.val)
        self.makeList(root.right, res)

