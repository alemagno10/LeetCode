# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()

        def search(row):
            l, r = 0, cols-1
            res = -1

            while l <= r:
                col = (r+l)//2
                if binaryMatrix.get(row, col):
                    r = col-1
                    res = col
                else:
                    l = col+1
            return res

        res = 1e5
        for row in range(rows):
            index = search(row)
            if index == 0:
                return 0
            if index >= 0:
                res = min(res, index)
        
        return res if res != 1e5 else -1
