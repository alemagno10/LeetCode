class ExamRoom:
    def __init__(self, n: int):
        self.total_seats = n
        self.occupied = []

    def seat(self) -> int:
        if len(self.occupied) == 0:
            self.occupied.append(0)
            return 0
        
        res, distance = 0, self.occupied[0]
        for l,r in zip(self.occupied, self.occupied[1:]):
            cur_dist = (-l+r)//2
            if cur_dist > distance:
                res, distance = (l+r)//2, cur_dist

        if self.total_seats - 1 - self.occupied[-1] > distance:
            res = self.total_seats - 1
        
        bisect.insort(self.occupied, res)
        return res

    def leave(self, p: int) -> None:
        self.occupied.remove(p)
          

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)
