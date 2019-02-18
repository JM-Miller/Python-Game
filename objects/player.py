from objects.game_object import GameObject

class Player(GameObject):

    x = 80
    y = 80

    xTileMapMove = 0
    yTileMapMove = 0

    width = 8
    height = 8

    weight = 1.2
    xAccel = 0.25

    xBrake = 1
    yBrake = 1
    
    xMomentum = 0
    yMomentum = 0

    xMomentumAdd = 0
    yMomentumAdd = 0

    xMaxSpeed = 5
    yMaxSpeed = 7.5

    jumpSpeed = 15.10
    
    mapScrollBuffer = 64

    sprite = None
    fill = "blue"

    block = False

    def Create(self, scrollBuffer):
        self.mapScrollBuffer = scrollBuffer
    
    def Render(self, canvas):
        canvas.create_rectangle(self.x, self.y, self.width + self.x, self.height + self.y, fill=self.fill)
        
    def Update(self, keysHeld, screenWidth=None, screenHeight=None, collisionObjects=None):

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
                    return True
                if selfBottom > collisionTop and selfBottom < collisionBottom:
                    return True

                    
                if selfBottom > collisionBottom and selfBottom < collisionTop:
                    return True
                if selfTop > collisionTop and selfTop < collisionBottom:
                    return True

        return False
            
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
                    return True
                if selfRight > collisionLeft and selfRight < collisionRight:
                    return True

                if selfRight > collisionRight and selfRight < collisionLeft:
                    return True
                if selfLeft > collisionLeft and selfLeft < collisionRight:
                    return True

        return False
            