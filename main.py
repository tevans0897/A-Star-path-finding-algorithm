from vacuumSetUp import *
from astar import *

actions = []
fullPath = []
totalNodesAccessed = 0
totalCost = 0

#Function to define starting states of each room
def getStartState(x):
    if x == 5:
        return "Dirty"
    else:
        return "Clean"


#Translate path returned by A* into actions for the vacuum
def translatePath(path):
    for i in range(len(path)):
        if i == len(path) - 1:
            actions.append("Suck")
            vacuum.Suck()
        else:
            curr = path[i]
            next = path[i+1]
            getAction(curr[0], next[0])
#Function ued by translate path to call vacuumn actions
def getAction(curr, next):
    diffX = next[0] - curr[0]
    diffY = next[1] - curr[1]
    if diffX != 0:
        if diffX > 0:
            actions.append("Right")
            vacuum.Right()
        else:
            actions.append("Left")
            vacuum.Left()
    else:
        if diffY > 0:
            actions.append("Up")
            vacuum.Up()
        else:
            actions.append("Down")
            vacuum.Down()


#Everything below this comment is the main body of the program

#Creating a 5x5 grid of rooms. Top row dirty, rest of rooms clean
grid = [[Room((j+1, 5-i), getStartState(5-i)) for j in range(5)] for i in range(5)]

#Create Vacuum starting at (1,1)
vacuum = Vacuum(grid[4][0], grid)

while len(vacuum.dirty_rooms) != 0:
    path, nodesAccessed = astarSearch(vacuum, grid)
    fullPath.append(path)
    translatePath(path)
    totalNodesAccessed += nodesAccessed

print("Optimal Path (point,f(n)):", fullPath)
print("Actions", actions)
print("Total Cost of Actions:", vacuum.totalCost)
print("Total Nodes Accessed:", totalNodesAccessed)
#print(vacuum.grid[0][0].__getattribute__("State"))


