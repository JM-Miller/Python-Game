from objects.game_object import GameObject

class Player(GameObject):

    x = 80
    y = 80

    width = 15
    height = 15

    weight = 1
    xAccel = 0.25

    xBrake = 1
    yBrake = 1

    xMaxSpeed = 5
    yMaxSpeed = 7.5

    jumpSpeed = 10
    
    sprite = None
    fill = "blue"

    block = False

    changeRoom = None

    def Create(self, changeRoom, scrollBuffer):
        self.mapScrollBuffer = scrollBuffer
        self.changeRoom = changeRoom
    
    def Render(self, canvas):
        canvas.create_rectangle(self.x, self.y, self.width + self.x, self.height + self.y, fill=self.fill)

    def Update(self, keysHeld, screenWidth=None, screenHeight=None, collisionObjects=None, mapFollowing=True):
        self.wantLeft = 37 in keysHeld
        self.wantJump = 38 in keysHeld
        self.wantRight = 39 in keysHeld    
        super().Update(keysHeld, screenWidth, screenHeight, collisionObjects, mapFollowing)
    

        
