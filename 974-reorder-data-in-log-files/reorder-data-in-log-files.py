class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter, digit = [], []
        for log in logs:
            ID, val = log.split(" ",1)
            if val[0].isdigit():
                digit.append(ID+" "+val)
            else:
                letter.append((ID,val))
        res = [x[0]+" "+x[1] for x in sorted(letter, key=lambda x: (x[1],x[0]))]
        res.extend(digit)
        return res
