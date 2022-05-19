from math import sqrt

#Class to establish rooms for the grid
class Room:
    def __init__(self, location, state):
        self.location = location
        self.neighbors = self.getNeighbors()
        self.State = state

    def get_location(self):
        return self.location

    def get_state(self):
        return self.State

    #function to get locations on neighboring rooms
    def getNeighbors(self):
        neighborsLocations = [(self.location[0] + 1, self.location[1]), (self.location[0] - 1, self.location[1]), (self.location[0], self.location[1] + 1), (self.location[0], self.location[1] - 1)]
        filtered = []

        for room in neighborsLocations:
            if 0 < room[0] <= 5 and 0 < room[1] <= 5:
                filtered.append(room)
        return filtered


#Class for Vacuum Agent. Initialized with start location and knowledge of dirty rooms
class Vacuum:
    #Intialization function
    def __init__(self, roomlocation, grid):
        self.grid = grid
        self.location = [roomlocation.location[0], roomlocation.location[1]]
        self.dirty_rooms = self.checkRooms(self.grid)
        #self.closestDirtyRoom = self.findFarthestDirtyRoom(self.dirty_rooms)
        self.closestDirtyRoom = self.findClosestDirtyRoom(self.dirty_rooms)
        self.totalCost = 0

    #move vacuum left
    def Left(self):
        self.location[0] = self.location[0] - 1
        self.totalCost += 1

    #move vacuum right
    def Right(self):
        self.location[0] = self.location[0] + 1
        self.totalCost += 1


    #move vacuum up
    def Up(self):
        self.location[1] = self.location[1] + 1
        self.totalCost += 1

    # move vacuum down
    def Down(self):
        self.location[1] = self.location[1] - 1
        self.totalCost += 1

    #Function for vacuum to clean room
    def Suck(self):
        self.getRoom().State = "Clean"
        self.dirty_rooms = self.checkRooms(self.grid)
        #self.closestDirtyRoom = self.findFarthestDirtyRoom(self.dirty_rooms)
        self.closestDirtyRoom = self.findClosestDirtyRoom(self.dirty_rooms)
        self.totalCost += 1

    #Compile list of rooms in grid that are dirty
    def checkRooms(self, grid):
        dirty_rooms = []
        for i in range(5):
            for j in range(5):
                if grid[i][j].__getattribute__("State") == "Dirty":
                    dirty_rooms.append(grid[i][j])
        return dirty_rooms

    #function to find closest dirty room by euclidean distance for h1
    def findClosestDirtyRoom(self, dirtyRooms):
        if len(dirtyRooms) == 0:
            closestRoom = dirtyRooms
        else:
            closestRoom = dirtyRooms[0]

        for room in dirtyRooms:
            if self.euclideanDistance(closestRoom) > self.euclideanDistance(room):
                closestRoom = room
        return closestRoom

    #function to find farthest dirty room by euclidean distance for h2
    def findFarthestDirtyRoom(self, dirtyRooms):
        if len(dirtyRooms) == 0:
            farthestRoom = dirtyRooms
        else:
            farthestRoom = dirtyRooms[0]

        for room in dirtyRooms:
            if self.euclideanDistance(farthestRoom) < self.euclideanDistance(room):
                farthestRoom = room
        return farthestRoom

    #function to calculate euclidean distance
    def euclideanDistance(self, room):
        return sqrt(pow(room.location[1]-self.location[1], 2) + pow(room.location[0]-self.location[0], 2))

    #function to return Room object on the grid
    def getRoom(self):
        return self.grid[5 - self.location[1]][self.location[0] - 1]


