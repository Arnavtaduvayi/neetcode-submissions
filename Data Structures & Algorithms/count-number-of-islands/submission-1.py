class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        seen = set()

        #go through list, if come across a 1 that we havent seen before,
        # run dfs on it. 
        #during dfs, add all island nodes to seen set. 

        cols = len(grid[0])
        rows = len(grid)

       
        def dfs (row, col):
            #base case: we run into a 0 or we are off the map
            if row < 0 or row > rows - 1 or col < 0 or col > cols - 1 :
                return
            if grid[row][col] == '0' or (row, col) in seen:
                return 

            seen.add((row, col))

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
            return None

        for i in range(rows):
            for j in range(cols) :
                if grid[i][j] == '1' and (i, j) not in seen:
                    islands += 1
                    dfs(i, j)

        return islands