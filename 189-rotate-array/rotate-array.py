class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        queue = []
        r = k % len(nums)
        l, q = 0,0

        for _ in range(len(nums)):
            queue.append(nums[r])   
            if l < k % len(nums):
                nums[r] = nums[l] 
            else:
                nums[r] = queue[q] 
                q = q+1

            l = l+1 if l < len(nums)-1 else 0
            r = r+1 if r < len(nums)-1 else 0