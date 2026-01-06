class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
    
        l, length = 0, 0
        isGreater = True
        for r in range(1,len(arr)):
            if arr[r-1] == arr[r]:
                l = r
            elif l+1 == r:
                isGreater = arr[r-1] > arr[r]
            elif (isGreater and arr[r-1] > arr[r]) or (not isGreater and arr[r-1] < arr[r]):
                l = r-1
            else:
                isGreater = not(isGreater)
            length = max(length, r-l+1)
        return length