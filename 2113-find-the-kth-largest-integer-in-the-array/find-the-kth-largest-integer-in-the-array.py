class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = map(lambda x: int(x), nums)
        nums = sorted(nums, reverse=True)
        return str(nums[k-1])