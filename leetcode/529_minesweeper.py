from typing import List

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        """
        Updates the Minesweeper board based on the click position.
        """
        def dfs(x, y):
            if board[x][y] != 'E':
                return
            mines = 0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] == 'M':
                    mines += 1
            if mines:
                board[x][y] = str(mines)
            else:
                board[x][y] = 'B'
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                        dfs(nx, ny)
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        x, y = click
        if board[x][y] == 'M':
            board[x][y] = 'X'
        else:
            dfs(x, y)
        return board

