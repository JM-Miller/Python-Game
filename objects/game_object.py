
class GameObject():

    x = 160
    y = 160
    width = 16
    height = 16

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
            if self.CheckForYCollision(collisionObjects):
                self.yMomentum = -self.jumpSpeed


        if not self.wantLeft and not self.wantRight:
            if self.xMomentum > 0.5:
                self.xMomentum -= self.xBrake
            else:
                if self.xMomentum < 0.5 and self.xMomentum > -0.5:
                    self.xMomentum = 0
                else:
                    if self.xMomentum < -0.5:
                        self.xMomentum += self.xBrake

        if self.xMomentum == 0 and self.CheckForXCollision(collisionObjects):
            self.xMomentum = 2
            self.x += self.xMomentum * -self.lastXDirection
            self.yMomentum = 0
        if self.yMomentum == 0 and self.CheckForYCollision(collisionObjects):
            self.yMomentum = 2
            self.y += self.yMomentum * -self.lastYDirection
            self.yMomentum = 0
        
        playerRightBuffer = self.x + self.width + self.mapScrollBuffer
        playerLeftBuffer = self.x - self.mapScrollBuffer
        playerBottomBuffer = self.y + self.height + self.mapScrollBuffer
        playerTopBuffer = self.y - self.mapScrollBuffer


        if not self.CheckForYCollision(collisionObjects):
            if playerBottomBuffer > screenWidth:
                self.yTileMapMove += self.yMomentum
            else:
                self.y += self.yMomentum
        else:
            self.yMomentum *= -1
            if self.yMomentum > 0:
                self.yMomentum = -1
            if self.yMomentum < 0:
                self.yMomentum = 1
            if not self.CheckForYCollision(collisionObjects):
                if playerBottomBuffer > screenWidth:
                    self.yTileMapMove += self.yMomentum
                else:
                    self.y += self.yMomentum
            self.yMomentum = 1

        playerXBuffer = playerLeftBuffer
        if self.xMomentum > 0:
            playerXBuffer = playerRightBuffer

        if not self.CheckForXCollision(collisionObjects):
            if playerXBuffer > screenWidth or playerXBuffer < 0:
                self.xTileMapMove += self.xMomentum
            else:
                self.x += self.xMomentum
        else:
            self.xMomentum *= -0.5
            if not self.CheckForXCollision(collisionObjects):
                if playerXBuffer > screenWidth or playerXBuffer < 0:
                    self.xTileMapMove += self.xMomentum
                else:
                    self.x += self.xMomentum
            self.xMomentum = 0

    def Create(self, changeRoom):
        pass


    def Destroy(self):
        self.isDestroyed = True
        self.block = False
        
    def CheckForYCollision(self, collisionObjects):
        for collision in collisionObjects:
            collisionTop = collision.y
            collisionBottom = collision.y + collision.height
            selfTop = self.y
            selfBottom = self.y + self.height
            if self.yTileMapMove != 0:
                selfTop += self.yMomentum
                selfBottom += self.yMomentum
            
            selfTop += self.yMomentum
            selfBottom += self.yMomentum

            collisionLeft = collision.x
            collisionRight = collision.x + collision.width
            selfLeft = self.x
            selfRight = self.x + self.width


            if selfLeft > collisionLeft and selfLeft < collisionRight or selfRight > collisionLeft and selfRight < collisionRight:

                if selfTop > collisionBottom and selfTop < collisionTop:
                    return collision
                if selfBottom > collisionTop and selfBottom < collisionBottom:
                    return collision

                    
                if selfBottom > collisionBottom and selfBottom < collisionTop:
                    return collision
                if selfTop > collisionTop and selfTop < collisionBottom:
                    return collision

        return None
            
    def CheckForXCollision(self, collisionObjects):
        for collision in collisionObjects:
            collisionTop = collision.y
            collisionBottom = collision.y + collision.height
            selfTop = self.y
            selfBottom = self.y + self.height

            collisionLeft = collision.x
            collisionRight = collision.x + collision.width
            selfLeft = self.x 
            selfRight = self.x + self.width
            
            if self.xTileMapMove != 0:
                selfLeft += 1
                selfRight += 1

            selfLeft += self.xMomentum
            selfRight += self.xMomentum

            if selfTop > collisionTop and selfTop < collisionBottom or selfBottom > collisionTop and selfBottom < collisionBottom:

                if selfLeft > collisionRight and selfLeft < collisionLeft:
                    return collision
                if selfRight > collisionLeft and selfRight < collisionRight:
                    return collision

                if selfRight > collisionRight and selfRight < collisionLeft:
                    return collision
                if selfLeft > collisionLeft and selfLeft < collisionRight:
                    return collision

        return None
            
        