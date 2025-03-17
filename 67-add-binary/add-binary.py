class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        res = ""

        for i in range(max(len(a),len(b))):
            c1 = a[len(a)-i-1] if i < len(a) else 0
            c2 = b[len(b)-i-1] if i < len(b) else 0

            curr = int(c1) + int(c2) + int(carry)
            if curr == 3:
                bit, carry = "1","1"
            elif curr == 2:
                bit, carry = "0","1"
            elif curr == 1:
                bit, carry = "1","0"
            else:
                bit, carry = "0","0"

            res = bit + res

        return carry+res if carry == "1" else res