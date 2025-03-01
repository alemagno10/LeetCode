class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]

        for curr in asteroids[1:]:
            while len(stack) > 0 and self.aboutToCollide(stack[-1], curr):
                if abs(stack[-1]) > abs(curr):
                    curr = 0
                    break
                elif abs(stack[-1]) == abs(curr):
                    curr = 0
                    stack.pop()
                    break
                else:
                    stack.pop()
            if curr:
                stack.append(curr)

        return stack
    
    def aboutToCollide(self,a,b):
        return (a > 0 and b < 0)