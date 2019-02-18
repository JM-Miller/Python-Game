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
        collision = self.CheckForXCollision(collisionObjects)
        if collision is None:
            collision = self.CheckForYCollision(collisionObjects)
        if collision is not None:
            self.DoSpecialAction(collision)
    
    def Render(self, canvas, xPixelOffset, yPixelOffset, xPosition, yPosition):
        self.x = xPosition * self.width + xPixelOffset
        self.y = yPosition * self.height + yPixelOffset

        canvas.create_rectangle(self.x, self.y, self.width + self.x, self.height + self.y, fill=self.fill)
        canvas.create_text(self.x + self.width / 2, self.y + self.height / 2, fill="black", font="sans-serif 8", text="!")



class WinTile(SpecialTile):
    fill = "yellow"

    changeRoom = None

    def Create(self, changeRoom):
        self.changeRoom = changeRoom

    def DoSpecialAction(self, collision):
        print('You Win!')
        self.changeRoom(0)