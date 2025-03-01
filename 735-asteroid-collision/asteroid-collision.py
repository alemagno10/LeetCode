class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]

        for ast in asteroids[1:]:
            stack.append(ast)
            while len(stack) > 1:
                curr, prev = stack[-1], stack[-2]
                
                if not self.aboutToCollide(prev, curr):
                    break
                else:
                    if abs(prev) > abs(curr):
                        stack.pop()
                        break
                    elif abs(prev) == abs(curr):
                        stack.pop()
                        stack.pop()
                        break
                    else:
                        stack.pop(-2)

        return stack
    
    def aboutToCollide(self,a,b):
        return (a > 0 and b < 0)