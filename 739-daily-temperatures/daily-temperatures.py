class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        days = [0]*len(temperatures)

        for i,T in enumerate(temperatures):
            while stack and stack[-1][1] < T:
                j = stack[-1][0]
                days[j] = i - j
                stack.pop()
            
            stack.append((i,T))
        
        return days