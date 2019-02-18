from objects.game_object import GameObject

class Enemy(GameObject):

    fill = "red"
    weight = 1
    x = 100
    y = 80
    xMaxSpeed = 10
    yMaxSpeed = 10
    xPixelOffset = 0
    yPixelOffset = 0
    

    player = None

    def Create(self, player):
        self.player = player
        

    def Update(self, keysHeld, xPixelOffset=0, yPixelOffset=0, screenWidth=None, screenHeight=None, collisionObjects=None, mapFollowing=False):
        self.x -= self.xPixelOffset - xPixelOffset
        self.y -= self.yPixelOffset - yPixelOffset
        self.xPixelOffset = xPixelOffset
        self.yPixelOffset = yPixelOffset
        super().Update(keysHeld, screenWidth, screenHeight, collisionObjects, mapFollowing)


