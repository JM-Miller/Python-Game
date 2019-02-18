
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

    xTileMapMove = 0
    yTileMapMove = 0

    sprite = None
    fill = "red"

    block = True

    
    def Render(self, canvas):
        canvas.create_rectangle(x, y, self.width, self.height, fill=self.fill)
        
    def Update(self, keysHeld, screenWidth=None, screenHeight=None, collisionObjects=None):
        pass

    def Create(self, changeRoom):
        pass


    def Destroy(self):
        pass
        
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
            
        