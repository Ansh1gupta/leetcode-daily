class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack=[]
        temp=[]
        for i in asteroids:
            if i>0:
                stack.append(i)
            elif i<0:
                temp.append(i)
                while stack and stack[-1]>0:
                    if stack[-1]==abs(i):
                        stack.pop()
                        temp.pop()
                        break
                    elif stack[-1]>abs(i):
                        temp.pop()
                        break
                    else:
                        stack.pop()
                if temp:
                    stack.append(temp.pop())
        return stack
             


