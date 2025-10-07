class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = math.inf

        for i in range(len(nums)):
            l, r = i+1, len(nums)-1
            while l < r:
                csum = nums[i] + nums[l] + nums[r]
                closest = min(closest, csum, key=lambda x: abs(target-x))   

                if csum < target:
                    l += 1
                elif csum > target:
                    r -= 1
                else:
                    break

        return closest