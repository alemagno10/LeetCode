import bisect

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)

    def add(self, val: int) -> int:
        kth = self.nums[len(self.nums)-self.k] if len(self.nums) > 0 else float('-inf')
        # if val >= kth:
        index = bisect.bisect_right(self.nums, val)
        self.nums.insert(index, val)
        return self.nums[len(self.nums)-self.k]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

# [2,3,4,4,5,5,8,9,10]


# [3,7,7,7,7,8,8,9,10] 