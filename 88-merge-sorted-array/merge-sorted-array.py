from copy import deepcopy

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        mycopy = deepcopy(nums1[:m])
        i, j = 0,0

        mycopy.append(math.inf)
        nums2.append(math.inf)

        while i < m or j < n:
            if mycopy[i] < nums2[j]:
                nums1[i+j] = mycopy[i]
                i += 1
            else:
                nums1[i+j] = nums2[j]
                j += 1



