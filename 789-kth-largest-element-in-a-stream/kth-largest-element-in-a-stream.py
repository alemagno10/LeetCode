import bisect

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)

    def add(self, val: int) -> int:
        nums = self.nums
        index = bisect.bisect_right(nums, val)
        nums.insert(index, val)
        return nums[len(nums)-self.k]
        