class Robot:
    def __init__(self, obstacles):
        self.x = 0
        self.y = 0
        self.direction = 0
        self.obstacles = obstacles
    
    def updateDirection(self, turn):
        if turn == -1:
            self.direction = (self.direction + 1) % 4
        if turn == -2:
            self.direction = (self.direction - 1) % 4
    
    def distFromOrigin(self):
        return self.x**2 + self.y**2
    
    def move(self, steps):
        if self.direction == 0:
            for _ in range(steps):
                if (self.x, self.y+1) in self.obstacles:
                    return 
                self.y += 1 
        if self.direction == 1:
            for _ in range(steps):
                if (self.x+1, self.y) in self.obstacles:
                    return
                self.x += 1 
        if self.direction == 2:
            for _ in range(steps):
                if (self.x, self.y-1) in self.obstacles:
                    return
                self.y -= 1 
        if self.direction == 3:
            for _ in range(steps):
                if (self.x-1, self.y) in self.obstacles:
                    return
                self.x -= 1 
        

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        robot = Robot(set([tuple(x) for x in obstacles]))

        distance = 0
        for command in commands:
            if command < 0:
                robot.updateDirection(command)
            else:
                robot.move(command)
                distance = max(distance, robot.distFromOrigin())
        
        return distance


