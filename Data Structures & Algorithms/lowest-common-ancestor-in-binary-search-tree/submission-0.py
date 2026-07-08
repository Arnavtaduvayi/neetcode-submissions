# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #find p and q from the root, add all accessed numbers to get to those numbers into a hashmap? 
        #Then, find all numbers in the hashmap with 2 instances, find the least of those and that is the answer. 

        #or, they must both be on the right, which is when we move right
        #or, they're both on the left, which is when we move left.
        #if we reach one where they are on opposite sides, then that is our LCA. 
        #At any point, if our tracker (curr), == p or q, that is our LCA. 

        curr = root

        while curr :
            if p.val > curr.val and q.val > curr.val :
                curr = curr.right
            if p.val < curr.val and q.val < curr.val :
                curr = curr.left
            if p.val == curr.val :
                return curr
            elif q.val == curr.val :
                return curr
            if p.val < curr.val and q.val > curr.val :
                return curr
            if p.val > curr.val and q.val < curr.val :
                return curr
