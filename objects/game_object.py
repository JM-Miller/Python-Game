
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

    sprite = None
    fill = "red"

    block = True

    
    def Render(self, canvas):
        canvas.create_rectangle(x, y, self.width, self.height, fill=self.fill)
        
    def Update(self, keysHeld, screenWidth=None, screenHeight=None, collisionObjects=None):
        pass

    def Create(self):
        pass


    def Destroy(self):
        pass
        