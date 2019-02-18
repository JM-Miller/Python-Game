from objects.game_object import GameObject

class Player(GameObject):

    x = 100
    y = 100
    width = 16
    height = 16

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

    sprite = None
    fill = "blue"

    block = False

    
    def Render(self, canvas):
        canvas.create_rectangle(self.x, self.y, self.width + self.x, self.height + self.y, fill=self.fill)
        
    def Update(self, keysHeld, collisionObjects=None):

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

        if not self.CheckForYCollision(collisionObjects):
            self.y += self.yMomentum
        else:
            self.yMomentum = 1
            if not self.CheckForYCollision(collisionObjects):
                self.y += 1

        if not self.CheckForXCollision(collisionObjects):
            self.x += self.xMomentum
        else:
            self.xMomentum = 1
            if not self.CheckForXCollision(collisionObjects):
                self.x += 1


    def CheckForYCollision(self, collisionObjects):
        for collision in collisionObjects:
            collisionTop = collision.y
            collisionBottom = collision.y + collision.height
            selfTop = self.y + self.yMomentum
            selfBottom = self.y + self.height + self.yMomentum
            
            collisionLeft = collision.x
            collisionRight = collision.x + collision.width
            selfLeft = self.x
            selfRight = self.x + self.width


            if selfLeft > collisionLeft and selfLeft < collisionRight or selfRight > collisionLeft and selfRight < collisionRight:

                if selfTop > collisionBottom and selfTop < collisionTop:
                    print("Collision on Top of Player!")
                    return True
                if selfBottom > collisionTop and selfBottom < collisionBottom:
                    print("Collision on Bottom of Player!")
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
            selfLeft = self.x + self.xMomentum
            selfRight = self.x + self.width + self.xMomentum

            if selfTop > collisionTop and selfTop < collisionBottom or selfBottom > collisionTop and selfBottom < collisionBottom:

                if selfLeft > collisionRight and selfLeft < collisionLeft:
                    print("Collision on Left of Player!")
                    return True
                if selfRight > collisionLeft and selfRight < collisionRight:
                    print("Collision on Right of Player!")
                    return True

        return False
            