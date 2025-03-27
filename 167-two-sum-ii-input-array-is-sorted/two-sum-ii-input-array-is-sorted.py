class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def search(diff, start, end):
            while end >= start:
                mid = math.floor((end+start)/2)
                if numbers[mid] == diff:
                    return mid
                elif numbers[mid] < diff:
                    start = mid+1
                else:
                    end = mid-1
            return -1

        for i,n in enumerate(numbers):
            j = search(target-n, i+1, len(numbers)-1)
            if j > -1:
                return [i+1, j+1]