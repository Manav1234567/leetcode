class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        counter = 0

        for i in range(rows):
            for j in range(cols):
                stack = []

                if grid[i][j] == "1":
                    counter += 1
                    stack.append((i, j))

                while stack:
                    a, b = stack.pop()
                    grid[a][b] = "0"

                    if a >= 1 and grid[a - 1][b] == "1": 
                        stack.append((a - 1, b))
                    if b >= 1 and grid[a][b - 1] == "1": 
                        stack.append((a, b - 1))
                    if a < rows - 1 and grid[a + 1][b] == "1": 
                        stack.append((a + 1, b))
                    if b < cols - 1 and grid[a][b + 1] == "1": 
                        stack.append((a, b + 1))

        return counter