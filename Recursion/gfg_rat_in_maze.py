class Solution:
    def solve(self, maze, row, col, n, subset, ans, visited):
        if row == n-1 and col == n-1:
            ans.append("".join(subset))
            return

        visited[row][col] = True

        if row+1 < n and maze[row+1][col] == 1 and not visited[row+1][col]:
            subset.append("D")
            self.solve(maze, row+1, col, n, subset, ans, visited)
            subset.pop()

        if col+1 < n and maze[row][col+1] == 1 and not visited[row][col+1]:
            subset.append("R")
            self.solve(maze, row, col+1, n, subset, ans, visited)
            subset.pop()

        if row-1 >= 0 and maze[row-1][col] == 1 and not visited[row-1][col]:
            subset.append("U")
            self.solve(maze, row-1, col, n, subset, ans, visited)
            subset.pop()

        if col-1 >= 0 and maze[row][col-1] == 1 and not visited[row][col-1]:
            subset.append("L")
            self.solve(maze, row, col-1, n, subset, ans, visited)
            subset.pop()

        visited[row][col] = False

    def ratInMaze(self, maze: list[list[int]]) -> list[str]:
        subset = []
        ans = []
        n = len(maze)

        if n == 0 or maze[0][0] == 0 or maze[n-1][n-1] == 0:
            return ans

        visited = [[False] * n for _ in range(n)]

        self.solve(maze, 0, 0, n, subset, ans, visited)
        return sorted(ans)