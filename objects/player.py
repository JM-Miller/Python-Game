from objects.game_object import GameObject

class Player(GameObject):

    x = 80
    y = 80

    xTileMapMove = 0
    yTileMapMove = 0

    width = 15
    height = 15

    weight = 1
    xAccel = 0.25

    xBrake = 1
    yBrake = 1
    
    xMomentum = 0
    yMomentum = 0

    xMomentumAdd = 0
    yMomentumAdd = 0

    xMaxSpeed = 5
    yMaxSpeed = 7.5

    jumpSpeed = 10
    
    mapScrollBuffer = 64

    sprite = None
    fill = "blue"

    block = False

    lastXDirection = 1
    lastYDirection = 1

    changeRoom = None

    def Create(self, changeRoom, scrollBuffer):
        self.mapScrollBuffer = scrollBuffer
        self.changeRoom = changeRoom
    
    def Render(self, canvas):
        canvas.create_rectangle(self.x, self.y, self.width + self.x, self.height + self.y, fill=self.fill)
        
    def Update(self, keysHeld, screenWidth=None, screenHeight=None, collisionObjects=None):

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

        if self.yMomentum > self.yMaxSpeed:
            self.yMomentum = self.yMaxSpeed

        if self.xMomentum > self.xMaxSpeed:
            self.xMomentum = self.xMaxSpeed

        if 37 in keysHeld:
            if self.xMaxSpeed > -1 * self.xMomentum:
                self.xMomentum -= self.xAccel

        if 39 in keysHeld:
            if self.xMaxSpeed > self.xMomentum:
                self.xMomentum += self.xAccel

        if 38 in keysHeld:
            if self.CheckForYCollision(collisionObjects):
                self.yMomentum = -self.jumpSpeed


        if 37 not in keysHeld and 39 not in keysHeld:
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
            self.xMomentum *= -1
            if not self.CheckForXCollision(collisionObjects):
                if playerXBuffer > screenWidth or playerXBuffer < 0:
                        self.xTileMapMove += self.xMomentum
                else:
                    self.x += self.xMomentum
            self.xMomentum = 0

        
