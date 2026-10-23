class MinStack:

    def __init__(self):
        self.arr=[]
        self.mini=[]
        self.min1=float("inf")
    def push(self, value: int) -> None:
        self.arr.append(value)
        if value<=self.min1:
            self.min1=value
            self.mini.append(value)
    def pop(self) -> None:
        l=len(self.arr)
        if l==0:
            return
        else:
            if self.arr[-1]==self.min1:
                self.arr.pop()
                self.mini.pop()
                if self.mini:
                    self.min1=self.mini[-1]
                else:
                    self.min1=float("inf")
            else:
               self.arr.pop()     
    def top(self) -> int:
        l=len(self.arr)
        if l==0:
            return
        else:
            return self.arr[-1]

    def getMin(self) -> int:
        if self.min1==float("inf"):
            return 
        else:
            return self.min1

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()