from objects.game_object import GameObject

class Enemy(GameObject):

    fill = "red"
    weight = 1
    x = 180
    y = 80
    width = 17
    height = 17
    xMaxSpeed = 10
    yMaxSpeed = 10
    xPixelOffset = 0
    yPixelOffset = 0

    collisionX = 0
    collisionY = 0

    startHealth = 100
    currentHealth = 100
    showHealth = False
    framesSinceHealthShown = 0
    framesToShowHealth = 90

    damageDealt = 10
    damageTaken = 10

    block = False

    playerObject = None

    def Create(self, player):
        self.playerObject = player
        

    def Update(self, keysHeld, xPixelOffset=0, yPixelOffset=0, screenWidth=None, screenHeight=None, collisionObjects=None, mapFollowing=False):
        if self.isDestroyed:
            return

        if self.showHealth:
            self.framesSinceHealthShown += 1
        if self.framesSinceHealthShown > self.framesToShowHealth:
            self.showHealth = False
            self.framesSinceHealthShown = 0

        xReset = self.x
        xOffsetReset = self.xPixelOffset
        self.xPixelOffset -= xPixelOffset

        self.x += self.xPixelOffset - xPixelOffset
        self.y += self.yPixelOffset - yPixelOffset
        self.xPixelOffset = xPixelOffset
        self.yPixelOffset = yPixelOffset

        playerCollision = self.CheckForCollision([self.playerObject])[0]

        if playerCollision is not None: 
            if self.playerObject.y >= self.y: 
                self.playerObject.xMomentum = -self.playerObject.xMomentum
                self.playerObject.TakeDamage(self.damageDealt)
                # self.playerObject.TakeDamage((self.xMomentum + 1) * self.damageDealt)
            else:
                if self.playerObject.x <= self.x:
                    self.xMomentum = self.playerObject.width
                if self.playerObject.x >= self.x:
                    self.xMomentum = -self.playerObject.width
                # self.TakeDamage((self.playerObject.yMomentum + 1) * self.damageTaken)
                # self.xMomentum = self.xMaxSpeed
                self.TakeDamage(self.damageTaken)
        super().Update(keysHeld, screenWidth, screenHeight, collisionObjects, mapFollowing)

        
        # self.x = xReset

    def Render(self, canvas):
        if self.isDestroyed:
            return
        
        xReset = self.x
        self.x += self.xPixelOffset
        

        super().Render(canvas)
        if self.showHealth:
            healthPercent = self.currentHealth / self.startHealth
            healthBarWidth = self.width * healthPercent + 2
            canvas.create_rectangle(self.x + (self.width / 2) - (healthBarWidth / 2), self.y - 5, self.x + (self.width / 2) + (healthBarWidth / 2), self.y - 2, fill="green")
        self.x = xReset

    def TakeDamage(self, damage):
        self.showHealth = True
        self.currentHealth -= damage
        if self.currentHealth < 0:
            self.Destroy()


