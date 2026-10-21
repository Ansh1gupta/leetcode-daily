class Solution:
    def solve(self,col,row,lower,upper,ans,board,n):
        if col==n:
            ans.append(board[:])
            return
        for i in range(n):
            if row[i]==0 and lower[i+col]==0 and upper[n-1+col-i]==0:
                board[i]=board[i][:col]+"Q"+board[i][col+1:]
                row[i]=1
                lower[i+col]=1
                upper[n-1+col-i]=1
                self.solve(col+1,row,lower,upper,ans,board,n)
                board[i]=board[i][:col]+"."+board[i][col+1:]
                row[i]=0
                lower[i+col]=0
                upper[n-1+col-i]=0
    def solveNQueens(self, n: int) -> list[list[str]]:
        ans=[]
        row=[0]*n
        lower=[0]*(2 *n-1)
        upper=[0]*(2*n-1)
        board=["." * n for i in range(n)]
        self.solve(0,row,lower,upper,ans,board,n)
        return ans
        