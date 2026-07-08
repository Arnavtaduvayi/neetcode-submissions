# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        qu = deque([p])
        que = deque([q])

        com = []
        comp = []

        while qu :

            for i in range (len(qu)):
                popped = qu.popleft()
                if popped: 
                    com.append(popped.val)
                else: 
                    com.append(popped)
                if popped :
                    qu.append(popped.left)
                    qu.append(popped.right)
            
        while que :

            for i in range (len(que)):
                popped = que.popleft()
                if popped: 
                    comp.append(popped.val)
                else: 
                    comp.append(popped)
                if popped :
                    que.append(popped.left)
                    que.append(popped.right)
        
        return com == comp
