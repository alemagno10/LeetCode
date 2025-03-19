class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        possibleRes = set(arr)
        prev = set() 

        for num in arr:
            curr = set({num})
            for p in prev:
                curr.add(num|p)
            possibleRes.update(curr)
            prev = curr

        return len(possibleRes)


