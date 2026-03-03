class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []

        for i,p1 in enumerate(prices):
            while stack and p1 <= stack[-1][0]:
                p2, j = stack.pop()
                prices[j] = p2-p1
            stack.append((p1,i))
        
        return prices

        