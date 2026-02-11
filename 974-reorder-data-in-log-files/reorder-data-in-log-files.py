class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter, digit = [], []
        for log in logs:
            ID, val = log.split(" ",1)
            if val[0].isdigit():
                digit.append(log)
            else:
                letter.append((ID,val,log))
        letter.sort(key=lambda x: (x[1],x[0]))
        return [x[2] for x in letter] + digit
