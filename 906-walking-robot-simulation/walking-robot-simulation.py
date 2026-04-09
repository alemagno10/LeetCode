class Robot:
    def __init__(self, obstacles):
        self.x = 0
        self.y = 0
        self.direction = 0
        self.moves = [(0,1), (1,0), (0,-1), (-1,0)]
        self.obstacles = obstacles
    
    def updateDirection(self, turn):
        if turn == -1:
            self.direction = (self.direction + 1) % 4
        if turn == -2:
            self.direction = (self.direction - 1) % 4
    
    def distFromOrigin(self):
        return self.x**2 + self.y**2
    
    def move(self, steps):
        dx, dy = self.moves[self.direction]
        for _ in range(steps):
            if (self.x+dx, self.y+dy) in self.obstacles:
                return 
            self.x += dx 
            self.y += dy 

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        robot = Robot(set(map(tuple, obstacles)))

        distance = 0
        for command in commands:
            if command < 0:
                robot.updateDirection(command)
            else:
                robot.move(command)
                distance = max(distance, robot.distFromOrigin())
        
        return distance