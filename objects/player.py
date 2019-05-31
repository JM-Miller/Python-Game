from objects.game_object import GameObject

class Player(GameObject):

    x = 80
    y = 80

    width = 15
    height = 15

    weight = 1
    xAccel = 0.5
    yAccel = 0.5

    xBrake = 1
    yBrake = 1

    xMaxSpeed = 3
    yMaxSpeed = 3
    
    xMaxAccel = 5
    yMaxAccel = 5


    startHealth = 100
    currentHealth = 100
    showHealth = False
    framesSinceHealthShown = 0
    framesToShowHealth = 90
    
    sprite = None
    fill = "blue"

    block = False

    changeRoom = None

    def Create(self, changeRoom, scrollBuffer):
        self.mapScrollBuffer = scrollBuffer
        self.changeRoom = changeRoom
    
    def Render(self, canvas):
        if self.isDestroyed:
            return
        
        if self.showHealth:
            self.framesSinceHealthShown += 1
        if self.framesSinceHealthShown > self.framesToShowHealth:
            self.showHealth = False
            self.framesSinceHealthShown = 0

        canvas.create_rectangle(self.x, self.y, self.width + self.x, self.height + self.y, fill=self.fill)
        
        if self.showHealth:
            healthPercent = self.currentHealth / self.startHealth
            healthBarWidth = self.width * healthPercent + 2
            canvas.create_rectangle(self.x + (self.width / 2) - (healthBarWidth / 2), self.y - 5, self.x + (self.width / 2) + (healthBarWidth / 2), self.y - 2, fill="green")


    def Update(self, keysHeld, screenWidth=None, screenHeight=None, collisionObjects=None, mapFollowing=True):
        if self.isDestroyed:
            return

        self.wantLeft = 37 in keysHeld
        self.wantUp = 38 in keysHeld
        self.wantRight = 39 in keysHeld    
        self.wantDown = 40 in keysHeld   
        self.wantActivate = 32 in keysHeld 

        super().Update(keysHeld, screenWidth, screenHeight, collisionObjects, mapFollowing)
    

    def TakeDamage(self, damage):
        self.showHealth = True
        self.currentHealth -= damage
        if self.currentHealth < 0:
            self.changeRoom(0)

