class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        for i in range (9):
            checked = set()
            for each in board[i]:
                if each == ".":
                    continue
                if each in checked:
                    return False
                checked.add(each)

        for i in range(9):
            checked = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] in checked:
                    return False
                else:
                    checked.add(board[j][i])

        starts = [(0,0), (3, 0), (6,0),(0,3), (3,3), (6,3), (0, 6), (3,6), (6,6)]

        for i, j in starts:
            checked = set()
            for row in range (i, i+3):
                for col in range (j, j+3):
                    if board[row][col] in checked:
                        return False
                    elif board[row][col] != ".":
                        checked.add(board[row][col])
        return True
