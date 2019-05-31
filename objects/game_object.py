
class GameObject():

    x = 160
    y = 160
    width = 15
    height = 15

    weight = 0

    xAccel = 0
    yAccel = 0
    
    xBrake = 1
    yBrake = 1
    
    xMomentum = 0
    yMomentum = 0

    xMomentumAdd = 0
    yMomentumAdd = 0

    xMaxSpeed = 0
    yMaxSpeed = 0
    
    xMaxAccel = 0
    yMaxAccel = 0

    xTileMapMove = 0
    yTileMapMove = 0
    
    lastXDirection = 1
    lastYDirection = 1

    sprite = None
    fill = "pink"

    block = True

    wantRight = False
    wantLeft = False
    wantJump = False

    isDestroyed = False

    mapScrollBuffer = 64

    
    def Render(self, canvas):
        if self.isDestroyed:
            return

        canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill=self.fill)
        
        
    def Update(self, keysHeld, screenWidth=None, screenHeight=None, collisionObjects=None, mapFollowing=False):
        if self.isDestroyed:
            return

        if self.xMomentum > 0:
            lastXDirection = 1
        if self.xMomentum < 0:
            lastXDirection = -1
            
        if self.xMomentum == 0:
            lastXDirection = 0
        
        if self.yMomentum == 0:
            lastYDirection = 0
            
        if self.yMomentum > 0:
            lastYDirection = 1
        if self.yMomentum < 0:
            lastYDirection = -1

        if self.xMomentum > self.xMaxSpeed:
            self.xMomentum = self.xMaxSpeed

        if self.wantLeft:
            if self.xMaxSpeed > -1 * self.xMomentum:
                if self.xMomentum > -self.xMaxAccel:
                    self.xMomentum -= self.xAccel

        if self.wantRight:
            if self.xMaxSpeed > self.xMomentum:
                if self.xMomentum < self.xMaxAccel:
                    self.xMomentum += self.xAccel

        if self.wantJump:
            if self.CheckForCollision(collisionObjects, 0, self.height / 2):
                self.yMomentum = -self.jumpSpeed
                print(self.yMomentum)


        if not self.wantLeft and not self.wantRight:
            if self.xMomentum > 0.5:
                self.xMomentum -= self.xBrake
            else:
                if self.xMomentum < 0.5 and self.xMomentum > -0.5:
                    self.xMomentum = 0
                else:
                    if self.xMomentum < -0.5:
                        self.xMomentum += self.xBrake

        
        playerRightBuffer = self.x + self.width + self.mapScrollBuffer - self.xTileMapMove
        playerLeftBuffer = self.x - self.mapScrollBuffer - self.xTileMapMove
        playerBottomBuffer = self.y + self.height + self.mapScrollBuffer
        playerTopBuffer = self.y - self.mapScrollBuffer

        if self.yMomentum >= self.height:
            yDir = 1
            if self.yMomentum < 0:
                yDir = -1
            if not self.CheckForCollision(collisionObjects, 0, 1):
                self.y += self.yMomentum
            else:
                self.yMomentum = 0
        else:
            if not self.CheckForCollision(collisionObjects, 0, self.yMomentum):
                self.y += self.yMomentum
            else:
                self.yMomentum = 0

        if self.xMomentum >= self.width or self.xMomentum <= -self.width:
            xDir = 1
            if self.xMomentum < 0:
                xDir = -1
            if not self.CheckForCollision(collisionObjects, xDir):
                if playerRightBuffer > screenWidth or playerLeftBuffer < 0 and (self.xMomentum >= 1 or self.xMomentum <= -1):
                    self.xTileMapMove += self.xMomentum
                else:
                    self.x += self.xMomentum
            else:
                self.xMomentum = 0
        else:
            if not self.CheckForCollision(collisionObjects, self.xMomentum):
                    self.x += self.xMomentum
            else:
                self.xMomentum = 0

    def Create(self, changeRoom):
        pass


    def Destroy(self):
        self.isDestroyed = True
        self.block = False
        
    def CheckForCollision(self, collisionObjects, xAdd=0, yAdd=0):
        selfCheckX = self.x + xAdd
        selfCheckY = self.y + yAdd
        for collision in collisionObjects:
            collisionTop = collision.y
            collisionBottom = collision.y + collision.height
            selfTop = selfCheckY
            selfBottom = selfCheckY + self.height

            collisionLeft = collision.x
            collisionRight = collision.x + collision.width
            selfLeft = selfCheckX 
            selfRight = selfCheckX + self.width
            
            if (selfTop >= collisionTop and selfTop <= collisionBottom and selfLeft >= collisionLeft and selfLeft <= collisionRight):
                return collision

            if (selfBottom <= collisionBottom and selfBottom >= collisionTop and selfLeft >= collisionLeft and selfLeft <= collisionRight):
                return collision

            if (selfBottom <= collisionBottom and selfBottom >= collisionTop and selfRight <= collisionRight and selfRight >= collisionLeft): 
                return collision

            if (selfTop <= collisionTop and selfTop >= collisionBottom and selfRight <= collisionRight and selfRight >= collisionLeft):
                return collision


        return None
            
        