class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        def dfs(start,end,turn):
            t = 1 if turn else -1

            if start == end:
                return nums[end]*t
            
            pickStart = dfs(start+1, end, not turn) + nums[start]*t
            pickEnd = dfs(start, end-1, not turn) + nums[end]*t

            if turn:
                return max(pickStart, pickEnd)
            return min(pickStart, pickEnd)
            
        return dfs(0,len(nums)-1,True) >= 0