from objects.game_object import GameObject
  
class Tile(GameObject):

    width = 16
    height = 16
    weight = 0
    xOrigin = 0
    yOrigin = 0
    fill = "black"
    block = False
    special = False

    
    def Render(self, canvas, xPixelOffset, yPixelOffset, xPosition, yPosition):
        pass

class SolidTile(Tile):

    block = True
    
    def Render(self, canvas, xPixelOffset, yPixelOffset, xPosition, yPosition):

        self.x = xPosition * self.width + xPixelOffset
        self.y = yPosition * self.height + yPixelOffset

        canvas.create_rectangle(self.x, self.y, self.width + self.x, self.height + self.y, fill=self.fill)

class EmptyTile(Tile):
    
    def Render(self, canvas, xPixelOffset, yPixelOffset, xPosition, yPosition):
        pass

      
class SpecialTile(Tile):
    fill = "purple"
    special = True

    def DoSpecialAction(self, collision):
        pass

    def Update(self, keysHeld, screenWidth=None, screenHeight=None, collisionObjects=None):
        collision = self.CheckForCollision(collisionObjects)

        if collision is not None:
            self.DoSpecialAction(collision)
    
    def Render(self, canvas, xPixelOffset, yPixelOffset, xPosition, yPosition):
        self.x = xPosition * self.width + xPixelOffset
        self.y = yPosition * self.height + yPixelOffset

        canvas.create_rectangle(self.x, self.y, self.width + self.x, self.height + self.y, fill=self.fill)



class WinTile(SpecialTile):
    fill = "yellow"

    width = 16
    height = 16

    changeRoom = None

    def Create(self, changeRoom):
        self.changeRoom = changeRoom

    def DoSpecialAction(self, collision):
        print('You Win!')
        self.changeRoom(0)

    def Render(self, canvas, xPixelOffset, yPixelOffset, xPosition, yPosition):
        super().Render(canvas, xPixelOffset, yPixelOffset, xPosition, yPosition)
        canvas.create_text(self.x + self.width / 2, self.y + self.height / 2, fill="black", font="sans-serif 8", text="!")



class BoostTile(SpecialTile):
    fill = "purple"

    changeRoom = None

    boostSpeed = 20
    boostDirection = 0

    width = 16
    height = 16

    text = "^"

    def __init__(self, changeRoom, direction, speed):
        self.boostSpeed = speed
        self.boostDirection = direction

        if direction == 0:
            self.text = "<"
            self.boostSpeed = speed
        if direction == 1:
            self.text = "^"
            self.boostSpeed = speed
        if direction == 2:
            self.text = ">"
        if direction == 3:
            self.text = "V"

    def Create(self, changeRoom=None):
        pass

    def DoSpecialAction(self, collision):

        if self.boostDirection == 0:
            collision.xMomentum -= self.boostSpeed 

        if self.boostDirection == 1:
            collision.yMomentum -= self.boostSpeed 

        if self.boostDirection == 2:
            collision.xMomentum += self.boostSpeed 

        if self.boostDirection == 3:
            collision.xMomentum += self.boostSpeed 


    def Render(self, canvas, xPixelOffset, yPixelOffset, xPosition, yPosition):
        super().Render(canvas, xPixelOffset, yPixelOffset, xPosition, yPosition)
        canvas.create_text(self.x + self.width / 2, self.y + self.height / 2, fill="black", font="sans-serif 8", text=self.text)

