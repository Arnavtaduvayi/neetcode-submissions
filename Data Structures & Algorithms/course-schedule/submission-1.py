class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        visited = {i: [] for i in range(numCourses)}
        dfsvisited = set()
        path = set()

        for crs, pre in prerequisites :
            visited[crs].append(pre)

        

        #to check for cycles, just use two sets. Path with active neighbors being explored. Visited for rest. 
        def dfs (node) :
            #base case: if node in path, return False (invalid).
            if node in path :
                return False
            if node in dfsvisited :
                return True
            path.add(node)
            
            for each in visited[node] :
                if not dfs(each) :
                    return False
            
            path.remove(node) 
            dfsvisited.add(node)

            return True

        for i in range(numCourses) :
            if not dfs(i) :
                return False

        return True

