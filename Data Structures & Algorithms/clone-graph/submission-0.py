"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #use BFS and clone each and every node one by one, use hashset to make sure we dont clone 
        #twice, append all neighbors into a newly created node. 

        #make the first one 

        if not node : 
            return None

        nbr = {}

        queue = collections.deque()
        queue.append(node)

        while queue :
            curr = queue.popleft()
            #our node is not made yet (first one)
            if curr not in nbr :
                #make a deep copy of current node, neighbors empty - need to copy from original
                newCurr = Node(curr.val, [])
                nbr[curr] = newCurr
                for each in curr.neighbors :
                    if each not in nbr :
                        nbr[each] = Node(each.val, [])
                        queue.append(each)
                    newCurr.neighbors.append(nbr[each])
            #our node already exists, lets copy all of the neighbors
            else :
                newCurr = nbr[curr]
                for each in curr.neighbors :
                    if each not in nbr :
                        nbr[each] = Node(each.val, [])
                        queue.append(each)
                    newCurr.neighbors.append(nbr[each])

        return nbr[node]




