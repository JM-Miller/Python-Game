
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
    wantUp = False
    wantDown = False
    wantActivate = False

    isDestroyed = False

    mapScrollBuffer = 64

    skipCollision = False

    
    def Render(self, canvas):
        if self.isDestroyed:
            return

        canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill=self.fill)
        
        
    def Update(self, keysHeld, currentHour, currentMinute, tileMapX, tileMapY, screenWidth=320, screenHeight=320, collisionObjects=None, mapFollowing=False):
        if self.isDestroyed:
            return


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

        if self.wantUp:
            if self.yMaxSpeed > -1 * self.yMomentum:
                self.yMomentum -= self.yAccel

        if self.wantDown:
            if self.yMaxSpeed > self.yMomentum:
                self.yMomentum += self.yAccel


        if not self.wantUp and not self.wantDown:
            if self.yMomentum > 0.5:
                self.yMomentum -= self.yBrake
            else:
                if self.yMomentum < 0.5 and self.yMomentum > -0.5:
                    self.yMomentum = 0
                else:
                    if self.yMomentum < -0.5:
                        self.yMomentum += self.yBrake

        if not self.wantLeft and not self.wantRight:
            if self.xMomentum > 0.5:
                self.xMomentum -= self.xBrake
            else:
                if self.xMomentum < 0.5 and self.xMomentum > -0.5:
                    self.xMomentum = 0
                else:
                    if self.xMomentum < -0.5:
                        self.xMomentum += self.xBrake

        playerRightBuffer = self.x + self.width + self.mapScrollBuffer
        playerLeftBuffer = self.x - self.mapScrollBuffer
        playerBottomBuffer = self.y + self.height + self.mapScrollBuffer
        playerTopBuffer = self.y - self.mapScrollBuffer

        playerXBuffer = playerLeftBuffer
        playerYBuffer = playerTopBuffer
        if self.xMomentum > 0:
            playerXBuffer = playerRightBuffer
        if self.yMomentum > 0:
            playerYBuffer = playerBottomBuffer

        if not self.CheckForCollision(collisionObjects, self.xMomentum)[0]:
            if playerXBuffer > screenWidth or playerXBuffer < 0:
                self.xTileMapMove += self.xMomentum
            else:
                self.x += self.xMomentum
        else:
            self.xMomentum *= -0.05
            if not self.CheckForCollision(collisionObjects, self.xMomentum)[0]:
                if playerXBuffer > screenWidth or playerXBuffer < 0:
                    self.xTileMapMove += self.xMomentum
                else:
                    self.x += self.xMomentum
            else:
                self.xMomentum = 0

            
        if not self.CheckForCollision(collisionObjects, 0, self.yMomentum)[0]:
            if playerYBuffer > screenHeight or playerYBuffer < 0:
                self.yTileMapMove += self.yMomentum
            else:
                self.y += self.yMomentum
        else:
            self.yMomentum *= -0.05
            if not self.CheckForCollision(collisionObjects, 0, self.yMomentum)[0]:
                if playerYBuffer > screenHeight or playerYBuffer < 0:
                    self.yTileMapMove += self.yMomentum
                else:
                    self.y += self.yMomentum
            self.yMomentum = 0


        if not self.wantLeft and not self.wantRight:
            self.xMomentum *= -0.05
        if not self.wantUp and not self.wantDown:
            self.yMomentum *= -0.05

        if self.wantActivate:
            activatedObject = self.CheckForCollision(collisionObjects, self.lastXDirection * 2, self.lastYDirection * 2)[0]
            if activatedObject:
                activatedObject.Activate([self], screenWidth, screenHeight)
                
        if self.xMomentum > 1:
            self.lastXDirection = 1
        if self.xMomentum < -1:
            self.lastXDirection = -1
            
        if self.yMomentum > 1:
            self.lastYDirection = 1
        if self.yMomentum < -1:
            self.lastYDirection = -1

    def Create(self, changeRoom):
        pass


    def Destroy(self):
        self.isDestroyed = True
        self.block = False

    def Activate(self, activator, screenWidth, screenHeight):
        pass
        
    def CheckForCollision(self, collisionObjects, xAdd=0, yAdd=0):
        selfCheckX = self.x + xAdd
        selfCheckY = self.y + yAdd

        if not collisionObjects:
            collisionObjects = []

        for collision in collisionObjects:
            if not collision.skipCollision:
                collisionTop = collision.y
                collisionBottom = collision.y + collision.height
                selfTop = selfCheckY
                selfBottom = selfCheckY + self.height

                collisionLeft = collision.x
                collisionRight = collision.x + collision.width
                selfLeft = selfCheckX 
                selfRight = selfCheckX + self.width

                colliding = False
                collidingLeft = False
                collidingRight = False
                collidingUp = False
                collidingDown = False
                
                # Top left
                if (selfTop >= collisionTop and selfTop <= collisionBottom and selfLeft >= collisionLeft and selfLeft <= collisionRight):
                    colliding = True
                    collidingLeft = True
                    collidingUp = True

                # Bottom left
                if (selfBottom <= collisionBottom and selfBottom >= collisionTop and selfLeft >= collisionLeft and selfLeft <= collisionRight):
                    colliding = True
                    collidingLeft = True
                    collidingDown = True

                # Bottom right
                if (selfBottom <= collisionBottom and selfBottom >= collisionTop and selfRight <= collisionRight and selfRight >= collisionLeft): 
                    colliding = True
                    collidingDown = True
                    collidingRight = True

                # Top right
                if (selfTop >= collisionTop and selfTop <= collisionBottom and selfRight <= collisionRight and selfRight >= collisionLeft):
                    colliding = True
                    collidingRight = True
                    collidingUp = True

                # Inside left
                if (selfTop <= collisionTop and selfBottom >= collisionBottom and selfLeft >= collisionLeft and selfLeft <= collisionRight):
                    colliding = True
                    collidingLeft = True

                # Inside right
                if (selfTop <= collisionTop and selfBottom >= collisionBottom and selfRight >= collisionLeft and selfRight <= collisionRight):
                    colliding = True
                    collidingRight = True

                # Inside top
                if (selfLeft <= collisionLeft and selfRight >= collisionRight and selfTop >= collisionTop and selfTop <= collisionBottom):
                    colliding = True
                    collidingUp = True

                # Inside bottom
                if (selfLeft <= collisionLeft and selfRight >= collisionRight and selfBottom >= collisionTop and selfBottom <= collisionBottom):
                    colliding = True
                    collidingDown = True

                if colliding:
                    return collision, collidingLeft, collidingUp, collidingRight, collidingDown 

        return None, False, False, False, False
            
        