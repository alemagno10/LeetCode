from copy import deepcopy

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k, m, n = (m+n-1), (m-1), (n-1)

        while n >= 0 or m >= 0:
            value1 = nums1[m] if m >= 0 else -math.inf
            value2 = nums2[n] if n >= 0 else -math.inf

            nums1[k] = max(value1, value2)
            k -= 1

            if value1 > value2:
                m -= 1
            else:
                n -= 1