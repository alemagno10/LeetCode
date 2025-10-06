class Solution:
    def intToRoman(self, num: int) -> str:
        romans = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        res = []
        romans_keys = ["M", "D", "C", "L", "X", "V", "I"]
        powers_of_ten = {"I", "X", "C", "M"}

        i = 0
        while num > 0:
            key = romans_keys[i]
            if num < romans[key]:
                i += 1
            elif str(num).startswith("4") or str(num).startswith("9"):
                num -= romans[romans_keys[i-1]] - romans[romans_keys[i+int(key not in powers_of_ten)]]  
                res.append(romans_keys[i+int(key not in powers_of_ten)] + romans_keys[i-1])
            else:
                num -= romans[key]
                res.append(key)
        
        return "".join(res)

            