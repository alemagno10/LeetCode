class Solution:
    def canJump(self, nums: List[int]) -> bool:
        steps_left = -1

        for i in range(1,len(nums)):
            steps_left = max(steps_left, nums[i-1])-1
            if steps_left < 0:
                return False
        return True















    #     # IS REACHABLE
    #     dp = [T, T, T, T, T]

    #     # STEPS LEFT
    #     i
    #     [3,2,1,0,4]
    #     [*,2,1,0, ]

    #            i
    #     [3,2,1,0,4]
    #    [-1,2,1,0,-1]

    #           i
    #    [2,3,1,1,4]
    #    [x,1,2,1,0]

    #     max(dp[i-1], nums[i-1])-1 



    #     dp = [? 2, ]




    #     dfs(i)

    #     for j range(i):
    #         if dp[j] >= i


    #             0
    #         1       2
    #     2   3   4   3
            