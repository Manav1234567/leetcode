class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        counter = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                stack = []

                if (grid[i][j] == "1" and visited[i][j] == 0):
                    counter += 1
                    stack.append((i, j))

                while stack != []:
                    a, b = stack.pop()
                    visited[a][b] = 1

                    if a >= 1 and grid[a - 1][b] == "1" and visited[a - 1][b] == 0: 
                        stack.append((a - 1, b))
                    if b >= 1 and grid[a][b - 1] == "1" and visited[a][b - 1] == 0: 
                        stack.append((a, b - 1))
                    if a < rows - 1 and grid[a + 1][b] == "1" and visited[a + 1][b] == 0: 
                        stack.append((a + 1, b))
                    if b < cols - 1 and grid[a][b + 1] == "1" and visited[a][b + 1] == 0: 
                        stack.append((a, b + 1))

        return counter