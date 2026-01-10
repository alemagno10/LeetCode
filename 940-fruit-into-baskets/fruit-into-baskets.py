class Basket:
    def __init__(self):
        self.type = -1
        self.cnt = 0
    
    def isEmpty(self):
        return self.cnt == 0
    
    def add(self, typ):
        self.type = typ
        self.cnt += 1
    
    def drop(self):
        self.cnt -= 1
        if self.cnt == 0:
            self.type = -1

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket1, basket2 = Basket(), Basket()
        res, l = 0, 0

        for r,fruit in enumerate(fruits):
            if basket1.isEmpty() or basket1.type == fruit:
                basket1.add(fruit)
                res = max(res, r-l+1)
            elif basket2.isEmpty() or basket2.type == fruit:
                basket2.add(fruit)
                res = max(res, r-l+1)
            else:
                while not basket1.isEmpty() and not basket2.isEmpty():
                    if fruits[l] == basket1.type:
                        basket1.drop()
                    else:
                        basket2.drop()
                    l += 1

                if basket1.isEmpty():
                    basket1.add(fruit)
                else:
                    basket2.add(fruit)

        return res
            