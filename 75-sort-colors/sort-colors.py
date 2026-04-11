class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def quicksort(low, high):
            if low < high:
                pivot = partition(low, high)
                quicksort(low, pivot-1)
                quicksort(pivot+1, high)

        def swap(a,b):
            nums[a], nums[b] = nums[b], nums[a]

        def partition(low, high):
            pivot, i = nums[high], low-1
            for j in range(low,high):
                if nums[j] <= pivot:
                    i+=1
                    swap(i,j)

            swap(i+1, high)
            return i+1
        
        quicksort(0, len(nums)-1)
            