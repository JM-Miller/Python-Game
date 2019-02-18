from objects.game_object import GameObject

class Enemy(GameObject):

    fill = "red"
    weight = 1
    x = 160
    y = 80
    width = 17
    height = 17
    xMaxSpeed = 10
    yMaxSpeed = 10
    xPixelOffset = 0
    yPixelOffset = 0

    block = False
    

    playerObject = None

    def Create(self, player):
        self.playerObject = player
        

    def Update(self, keysHeld, xPixelOffset=0, yPixelOffset=0, screenWidth=None, screenHeight=None, collisionObjects=None, mapFollowing=False):
        self.x -= self.xPixelOffset - xPixelOffset
        self.y -= self.yPixelOffset - yPixelOffset
        self.xPixelOffset = xPixelOffset
        self.yPixelOffset = yPixelOffset
        super().Update(keysHeld, screenWidth, screenHeight, collisionObjects, mapFollowing)

        playerCollisionX = self.playerObject.CheckForXCollision([self])
        playerCollisionY = self.playerObject.CheckForYCollision([self])

        if playerCollisionX is not None or playerCollisionY is not None: 
            if self.playerObject.y >= self.y: 
                self.playerObject.xMomentum = -self.playerObject.xMomentum
                self.DealDamage()
            else:
                self.xMomentum = self.playerObject.xMomentum + 1
                if self.playerObject.x < self.x:
                    self.x += self.playerObject.width
                if self.playerObject.x > self.x:
                    self.x -= self.width
                self.TakeDamage()

    def DealDamage(self):
        pass
        
    def TakeDamage(self):
        pass

