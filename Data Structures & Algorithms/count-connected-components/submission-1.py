class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # a fully connected graph should have n - 1 edges
        # num of edges can be counted by the num of elements in edges 
        
        #make adjacency list, do dfs on it until we find n vertices

        visited = set() 
        adjlist = {i : [] for i in range(n)}
        num = 0

        def dfs (node) :
            #base cases
            if node in visited :
                return False
            if len(visited) == n :
                return False
            visited.add(node)
            for each in adjlist[node] :
                dfs(each)

            return True


        for e0, e1 in edges : 
            adjlist[e1].append(e0)
            adjlist[e0].append(e1)


        for i in range(n) :
            if dfs(i) :
                num += 1

        
        return num
            


