class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr,l,mid,r):
            left, right = arr[l:mid+1], arr[mid+1:r+1]
            ap, lp, rp = l,0,0

            while lp < len(left) and rp < len(right): 
                if left[lp] < right[rp]:
                    arr[ap] = left[lp]
                    lp+=1
                else:
                    arr[ap] = right[rp]
                    rp+=1
                ap+=1
            
            while lp < len(left):
                arr[ap] = left[lp]
                ap, lp = ap+1, lp+1
            
            while rp < len(right):
                arr[ap] = right[rp]
                ap, rp = ap+1, rp+1


        def mergeSort(arr,l,r):
            if l == r:
                return arr

            mid = (l+r)//2
            mergeSort(arr,l,mid)
            mergeSort(arr,mid+1,r)  
            merge(arr,l,mid,r)
            return arr

        return mergeSort(nums,0,len(nums)-1)


