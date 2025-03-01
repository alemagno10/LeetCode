class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]

        for ast in asteroids[1:]:
            stack.append(ast)
            while len(stack) > 1:
                curr, prev = stack.pop(), stack.pop()
                
                if not self.aboutToCollide(prev, curr):
                    stack.append(prev)
                    stack.append(curr)
                    break
                else:
                    if abs(prev) > abs(curr):
                        stack.append(prev)
                        break
                    elif abs(prev) == abs(curr):
                        break
                    else:
                        stack.append(curr)

        return stack
    
    def aboutToCollide(self,a,b):
        return (a > 0 and b < 0)