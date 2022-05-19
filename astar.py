from vacuumSetUp import *

#priority queue utilized by a*
class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.movesSoFar = 0


    def isEmpty(self):
        return len(self.queue) == 0

    def insert(self, room, cost):
        self.queue.append((room, cost))

    #pop value from queue into the charted path
    def pop(self, path, current, grid):
        try:
            min = (current, 100)
            for i in range(len(self.queue)):
                if self.returnCoor(self.queue[i]) == self.returnCoor(min):
                    min = self.queue[i]
            path.append(min)
            self.queue.remove(min)
        except IndexError:
            print()
            exit()

    #get current value at top of priority queue
    def get(self, current, grid):
        try:
            min = (current, 100)
            for i in range(len(self.queue)):
                if self.returnCoor(self.queue[i]) in getRoom(current, grid).neighbors or self.returnCoor(self.queue[i]) == self.returnCoor(min):
                    if (self.returnCost(self.queue[i]) + self.movesSoFar) < (self.returnCost(min) + self.movesSoFar):
                        min = self.queue[i]
            self.movesSoFar+=1
            return min
        except IndexError:
            print()
            exit()

    def returnCoor(self, tupleInQueue):
        return tupleInQueue[0]

    #Function to retuen cost hueristic of a room in the queue for pop function
    def returnCost(self, tupleInQueue):
        return tupleInQueue[1]





#A* search to return shortest path to current goal
def astarSearch(vacuum, grid):
    fringe = PriorityQueue()
    path = []
    visited = []
    start = (vacuum.location[0], vacuum.location[1])
    goal = vacuum.closestDirtyRoom
    fringe.insert(start, getHeuristic(start, goal))
    visited.append(start)
    current = fringe.queue[0]

    while not fringe.isEmpty():
        current = fringe.get(current[0], grid)

        #print(current, '\n')

        if current[0] == goal.location:
            path.append(current)
            return path, len(visited)
        for neighbor in getRoom(current[0], grid).neighbors:
            if neighbor not in visited:
                fringe.insert(neighbor, getHeuristic(neighbor, goal))
                visited.append(neighbor)
        fringe.pop(path, current[0], grid)
    return path


def getHeuristic(room, goal):
    h = abs(goal.location[1] - room[1]) + abs(goal.location[0] - room[0])
    return h

#Function for distance of currently expanded node from start to add to h
#If all movement cost is 1 then, distance from start point will cover current total movement cost
def distanceFromStart(currentRoom, start):
    d = abs(currentRoom[1] - start[1]) + abs(currentRoom[0] - start[0])
    return d

#function to return room from grid to access data
def getRoom(current, grid):
    return grid[5-current[1]][current[0]-1]



