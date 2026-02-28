class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        stack = []

        for interval in intervals:
            if len(stack) == 0:
                stack.append(interval)
                continue
            curr = interval
            while stack and stack[-1][1] >= interval[0]:
                peek = stack.pop()
                curr = [peek[0], max(interval[1], peek[1])]
            stack.append(curr)

        return stack
                
