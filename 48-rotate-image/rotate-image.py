class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        k = 0
        end = len(matrix)-1
        for i in range(end-k):
            for j in range(end-k):
                matrix[i][j], matrix[end-j][end-i] = matrix[end-j][end-i], matrix[i][j]
            k += 1
        
        for i in range(int(len(matrix)/2)):
            matrix[i], matrix[end-i] = matrix[end-i], matrix[i]
        
