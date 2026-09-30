class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        l=len(matrix)
        r=len(matrix[0])
        c=l*r
        arr=[]
        top,left=0,0
        right=r-1
        bottom=l-1
        while(top<=bottom and left<=right):
          for i in range(left,right+1):
            arr.append(matrix[top][i])
          top+=1
          for i in range(top,bottom+1):
            arr.append(matrix[i][right])
          right-=1
          if top<=bottom:
            for i in range(right,left-1,-1):
              arr.append(matrix[bottom][i])
            bottom-=1
          if left<=right:
             for i in range(bottom,top-1,-1):
               arr.append(matrix[i][left])
             left+=1
        return arr


            