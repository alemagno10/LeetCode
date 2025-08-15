class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last, duplicates, j = nums[0],0,1

        def findNextValid(j):
            while j < len(nums) and (nums[j] == last or nums[j] == '_'):
                nums[j] = '_'
                j += 1
            return j

        for i in range(1,len(nums)):
            if nums[i] == last or nums[i] == '_':
                j = findNextValid(j)
                nums[i] = nums[j] if j < len(nums) else nums[i]
            else:
                j+=1
            last = nums[i] if nums[i] != '_' else last
        
        return len(nums) - nums.count("_")
