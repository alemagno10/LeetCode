from collections import defaultdict

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1, counter2 = Counter(nums1), Counter(nums2)
        res = []
        for k,v in counter1.items():
            if k in counter2:
                for i in range(min(v, counter2[k])):
                    res.append(k)
        return res