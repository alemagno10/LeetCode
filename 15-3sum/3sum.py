class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            start, end = i+1, len(nums)-1
            while start < end:
                tSum = nums[i] + nums[start] + nums[end]

                if tSum == 0:
                    res.append([nums[i], nums[start], nums[end]])
                
                if tSum <= 0:
                    start += 1
                    while start < end and nums[start] == nums[start-1]:
                        start += 1

                if tSum >= 0:
                    end -= 1      
                    while start < end and nums[end] == nums[end+1]:
                        end -= 1
        return res


