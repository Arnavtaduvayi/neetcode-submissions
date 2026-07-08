# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #I assume level order is basically just BFS. Let me attempt. 
        #append and popleft for queue
        if not root :
            return []
        q = deque([root])
        res = []

        while q :
            subres = []
            for i in range (len(q)) :
                node = q.popleft()
                subres.append(node.val)
                if node.left: 
                    q.append(node.left)
                if node.right: 
                    q.append(node.right)
            res.append(subres)

        return res