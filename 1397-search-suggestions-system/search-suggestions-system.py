class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = []
        products.sort()
        for i in range(len(searchWord)):
            res.append([])
            prefix = searchWord[:i+1]
            for w in products:
                if w.startswith(prefix):
                    res[i].append(w)
                if len(res[i]) == 3:
                    break
        return res