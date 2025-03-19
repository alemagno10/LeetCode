class Solution:
    def reverseBits(self, n: int) -> int:
        aux = 1
        res = [0]*32
        for i in range(32):
            res[i] = "1" if (n & aux) != 0 else "0"
            aux <<= 1
        return int("".join(res),2)