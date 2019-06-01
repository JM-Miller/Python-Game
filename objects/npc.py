from objects.game_object import GameObject
from objects.tilemap.tile import SolidTile, DoorTile

class NPC(GameObject):

    fill = "red"
    weight = 1
    width = 16
    height = 16
    xMaxSpeed = 10
    yMaxSpeed = 10

    xOrigin = 0
    yOrigin = 0

    xPixelOffset = 0
    yPixelOffset = 0

    changeRoom = None

    currentPath = None
    pathStepIndex = 0
    
    unactiveMaxTime = 20
    unactiveTime = 20

    id = 0

    block = True

    playerObject = None

    def __init__(self, id, changeRoom, x=0, y=0):
        self.changeRoom = changeRoom
        self.Create(id)
        self.xOrigin = x
        self.yOrigin = y

    def Create(self, id):
        self.id = id
        

    def Update(self, keysHeld, currentHour, currentMinute, tileX, tileY, screenWidth, screenHeight, collisionObjects=None, mapFollowing=False, xPixelOffset=0, yPixelOffset=0):
        if self.isDestroyed:
            return
        if self.currentPath != self.GetCurrentPath(currentHour,currentMinute):
            self.pathStepIndex = 0 
            self.currentPath = self.GetCurrentPath(currentHour,currentMinute)
        if self.currentPath and self.pathStepIndex < len(self.currentPath):

            if self.x > ((self.currentPath[self.pathStepIndex][0] * self.width) - self.xPixelOffset):
                self.xOrigin -= 1
            
            if self.x < ((self.currentPath[self.pathStepIndex][0] * self.width) - self.xPixelOffset):
                self.xOrigin += 1

            if self.y > ((self.currentPath[self.pathStepIndex][1] * self.height) - self.yPixelOffset):
                self.yOrigin -= 1
            
            if self.y < ((self.currentPath[self.pathStepIndex][1] * self.height) - self.yPixelOffset):
                self.yOrigin += 1


            if self.x == (self.currentPath[self.pathStepIndex][0] * self.width - self.xPixelOffset) and self.y == (self.currentPath[self.pathStepIndex][1] * self.height - self.yPixelOffset):
                if self.pathStepIndex < len(self.currentPath):
                    self.pathStepIndex += 1

        self.xPixelOffset = tileX
        self.yPixelOffset = tileY
        self.x = self.xOrigin - self.xPixelOffset
        self.y = self.yOrigin - self.yPixelOffset

        collisionObjects = filter(lambda colObj: type(colObj) is not SolidTile and colObj is not self, collisionObjects)
        collision = self.CheckForCollision(collisionObjects)

        if type(collision[0]) is DoorTile:
            self.unactiveTime -= 1
            if self.unactiveTime < 0:
                self.unactiveTime = self.unactiveMaxTime
                self.xOrigin = collision[0].targetX * self.width
                self.yOrigin = collision[0].targetY * self.height
                self.pathStepIndex += 1
                collision[0].Activate([self, collision[1], collision[2], collision[3], collision[4]], screenWidth, screenHeight)

        super().Update(keysHeld, currentHour, currentMinute, tileX, tileY, screenWidth, screenHeight, collisionObjects, mapFollowing)


    def Render(self, canvas):
        if self.isDestroyed:
            return

        canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill=self.fill)
        super().Render(canvas)
        canvas.create_text(self.x + self.width / 2, self.y + self.height / 2, fill="black", font="sans-serif 8", text=self.id)

    def Activate(self, collision, screenWidth, screenHeight):
        self.changeRoom(2, self.id)


    def GetCurrentPath(self, currentHour, currentMinute):
        if self.id == 2:
            if currentHour == 12:
                return [[31, 40], [31, 36], [37, 36], [37, 40]]
            elif currentHour == 14:
                return [[31, 40], [31, 36], [37, 36], [37, 40]]

        if self.id == 1:
            if currentHour == 12 and currentMinute > 5:
                return [[13, 3], [34, 40], [34, 38], [32, 38], [34, 41], [13, 5], [20, 5]]
        return None



