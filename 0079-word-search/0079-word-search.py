class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]

        def dfs(r, c, idx):
            if idx == len(word):
                return True
            
            if r < 0 or r >= m or c < 0 or c >= n:
                return False
            
            if visited[r][c] == True or board[r][c] != word[idx]:
                return False
            
            visited[r][c] = True

            found = (dfs(r+1, c, idx+1) or dfs(r, c+1, idx+1) or dfs(r-1, c, idx+1) or dfs(r, c-1, idx+1))

            visited[r][c] = False

            return found
        

        for r in range(m):
            for c in range(n):
                if dfs(r, c, 0):
                    return True
        return False