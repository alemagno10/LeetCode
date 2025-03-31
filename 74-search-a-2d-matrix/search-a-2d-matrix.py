class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        up, down = 0, len(matrix)-1

        while down > up:
            mid = (up+down)//2
            if matrix[mid][0] > target:
                down = mid-1
            elif matrix[mid][0] < target:
                up = mid+1
            else:
                return True
        
        row = up if target < matrix[down][0] else down 
        if target < matrix[row][0]:
            row-=1
        
        left, right = 0, len(matrix[0])-1

        while left <= right:
            mid = (left+right)//2
            if matrix[row][mid] > target:
                right = mid-1
            elif matrix[row][mid] < target:
                left = mid+1
            else:
                return True

        return False

        