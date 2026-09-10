class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # use BFS on the grid while going through it. 
        # for loop to go through each of the grid elements. 
        # if a 1 is detected, send it through BFS helper method -> add all connected    ones to a hashset so we dont visit them again. 

        if not grid :
            return 0
            
        visited = set()
        numIslands = 0

        def bfs(r, c) :
            queue = collections.deque()
            queue.append((r,c))
            while (queue) :
                ro, co = queue.popleft()
                if (ro+1 < len(grid)) and grid[ro+1][co] == "1" and (ro+1, co) not in visited:
                    visited.add((ro+1, co))
                    queue.append([ro+1, co])
                if (co + 1 < len(grid[0])) and grid[ro][co + 1] == "1" and (ro, co+1) not in visited:
                    visited.add((ro, co + 1))
                    queue.append([ro, co + 1])
                if (ro-1 >= 0) and grid[ro-1][co] == "1" and (ro-1, co) not in visited:
                    visited.add((ro-1, co))
                    queue.append((ro-1, co))
                if (co - 1 >= 0) and grid[ro][co - 1] == "1" and (ro, co-1) not in visited:
                    visited.add((ro, co - 1))
                    queue.append((ro, co - 1))

                
            
        for i in range (len(grid)) :
            for j in range (len(grid[0])) :
                if grid[i][j] == "1" :
                    if (i,j) not in visited :
                        numIslands += 1
                        bfs(i,j)

        return numIslands