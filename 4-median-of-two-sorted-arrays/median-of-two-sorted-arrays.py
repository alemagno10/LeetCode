class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0,0

        concat = []

        while i < len(nums1) or j < len(nums2):

            if i < len(nums1) and j < len(nums2):
                if nums1[i] < nums2[j]:
                    concat.append(nums1[i])
                    i += 1
                else:
                    concat.append(nums2[j])
                    j += 1
            
            elif i == len(nums1):
                concat.append(nums2[j])
                j += 1
            
            else:
                concat.append(nums1[i])
                i += 1
    
        if len(concat) % 2 == 0:
            mid = math.floor(len(concat)/2)
            return (concat[mid] + concat[mid-1]) / 2
        
        else:
            return concat[math.floor(len(concat)/2)]