class Solution:
    def canJump(self, nums: List[int]) -> bool:
        steps_left = -1

        for i in range(1,len(nums)):
            steps_left = max(steps_left, nums[i-1])-1
            if steps_left < 0:
                return False
        return True