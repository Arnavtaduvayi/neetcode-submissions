class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # start at each value bordering pacific, do dfs and mark any node that is accessible in pac
        #then, start at atlantic and do dfs. do same as above and update atl. 
        #If any explored node is accessible by pac and atl, then add that to result. 

        c = len(heights[0])
        r = len(heights)

        pac, atl = set(), set()


        def dfs(row, col, ocean, prevH):
            #check if r,c height >= prev 
            if row < 0 or col < 0 or row > r - 1 or col > c - 1 or (row, col) in ocean or heights[row][col] < prevH :
                return

            ocean.add((row, col))

            dfs(row - 1, col, ocean, heights[row][col])
            dfs(row, col - 1, ocean, heights[row][col])
            dfs(row, col + 1, ocean, heights[row][col])
            dfs(row + 1, col, ocean, heights[row][col])

        for i in range(c) :
            dfs(0, i, pac, -float('inf')) 

        for i in range(r) :
            dfs(i, 0, pac, -float('inf'))

        for i in range(c) :
            dfs(r-1, i, atl, -float('inf')) 

        for i in range(r) :
            dfs(i, c-1, atl, -float('inf'))

        result = []
        for i in range(r):
            for j in range(c) :
                if (i,j) in pac and (i,j) in atl :
                    k, l = (i,j)
                    result.append([k, l])

        return result
