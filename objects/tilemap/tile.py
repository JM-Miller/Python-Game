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

        if self.skipCollision:
            self.fill = "white"

        canvas.create_rectangle(self.x, self.y, self.width + self.x, self.height + self.y, fill=self.fill)

class EmptyTile(Tile):
    
    def Render(self, canvas, xPixelOffset, yPixelOffset, xPosition, yPosition):
        pass

      
class SpecialTile(Tile):
    fill = "purple"
    special = True

    def DoSpecialAction(self, collision, screenWidth, screenHeight):
        pass

    def Update(self, keysHeld, screenWidth=None, screenHeight=None, collisionObjects=None):
        collision = self.CheckForCollision(collisionObjects)

        if collision[0] is not None:
            # if collision[1]:
            #     print("LEFT")
            # if collision[2]:
            #     print("UP")
            # if collision[3]:
            #     print("RIGHT")
            # if collision[4]:
            #     print("DOWN")
            self.DoSpecialAction(collision, screenWidth, screenHeight)
    
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

    def DoSpecialAction(self, collision, screenWidth, screenHeight):
        print('You Win!')
        self.changeRoom(0)

    def Render(self, canvas, xPixelOffset, yPixelOffset, xPosition, yPosition):
        super().Render(canvas, xPixelOffset, yPixelOffset, xPosition, yPosition)
        canvas.create_text(self.x + self.width / 2, self.y + self.height / 2, fill="black", font="sans-serif 8", text="!")

class DoorTile(SpecialTile):
    fill = "gray"

    width = 16
    height = 16

    block = True

    changeRoom = None

    def __init__(self, changeRoom=None, x=0, y=0):
        self.targetX = x
        self.targetY = y

    def Create(self, changeRoom):
        self.changeRoom = changeRoom

    def Activate(self, collision, screenWidth, screenHeight):
        print('Warp!')
        collision[0].x = (self.targetX * self.width) - collision[0].xTileMapMove
        collision[0].y = (self.targetY * self.height) - collision[0].yTileMapMove
        # Left
        if collision[0].x < collision[0].mapScrollBuffer:
            diff = collision[0].mapScrollBuffer - ((collision[0].x + collision[0].xTileMapMove) - collision[0].width)
            collision[0].x = collision[0].mapScrollBuffer
            collision[0].xTileMapMove = -diff
            print(diff)

        # Right
        if collision[0].x > screenWidth - collision[0].mapScrollBuffer:
            diff = ((collision[0].x + collision[0].xTileMapMove) - collision[0].width) - (screenWidth - collision[0].mapScrollBuffer)
            collision[0].x = screenWidth - collision[0].mapScrollBuffer
            collision[0].xTileMapMove = diff
            print(diff)
            
        # Top
        if collision[0].y < collision[0].mapScrollBuffer:
            diff = collision[0].mapScrollBuffer - ((collision[0].y + collision[0].yTileMapMove) - collision[0].height)
            collision[0].y = collision[0].mapScrollBuffer
            collision[0].yTileMapMove = -diff
            print(diff)

        # Bottom
        if collision[0].y > screenHeight - collision[0].mapScrollBuffer:
            diff = ((collision[0].y + collision[0].yTileMapMove) - collision[0].height) - (screenHeight - collision[0].mapScrollBuffer)
            collision[0].y = screenHeight - collision[0].mapScrollBuffer
            collision[0].yTileMapMove = diff
            print(diff)


class WarpTile(SpecialTile):
    fill = "blue"

    width = 16
    height = 16

    targetX = 34
    targetY = 20

    changeRoom = None
    
    def __init__(self, changeRoom=None, x=0, y=0):
        self.targetX = x
        self.targetY = y

    def Create(self, changeRoom):
        self.changeRoom = changeRoom

    def DoSpecialAction(self, collision, screenWidth, screenHeight):
        print('Warp!')
        collision[0].x = (self.targetX * self.width) - collision[0].xTileMapMove
        collision[0].y = (self.targetY * self.height) - collision[0].yTileMapMove
        # Left
        if collision[0].x < collision[0].mapScrollBuffer:
            diff = collision[0].mapScrollBuffer - ((collision[0].x + collision[0].xTileMapMove) - collision[0].width)
            collision[0].x = collision[0].mapScrollBuffer
            collision[0].xTileMapMove = -diff
            print(diff)

        # Right
        if collision[0].x > screenWidth - collision[0].mapScrollBuffer:
            diff = ((collision[0].x + collision[0].xTileMapMove) - collision[0].width) - (screenWidth - collision[0].mapScrollBuffer)
            collision[0].x = screenWidth - collision[0].mapScrollBuffer
            collision[0].xTileMapMove = diff
            print(diff)
            
        # Top
        if collision[0].y < collision[0].mapScrollBuffer:
            diff = collision[0].mapScrollBuffer - ((collision[0].y + collision[0].yTileMapMove) - collision[0].height)
            collision[0].y = collision[0].mapScrollBuffer
            collision[0].yTileMapMove = -diff
            print(diff)

        # Bottom
        if collision[0].y > screenHeight - collision[0].mapScrollBuffer:
            diff = ((collision[0].y + collision[0].yTileMapMove) - collision[0].height) - (screenHeight - collision[0].mapScrollBuffer)
            collision[0].y = screenHeight - collision[0].mapScrollBuffer
            collision[0].yTileMapMove = diff
            print(diff)

    def Render(self, canvas, xPixelOffset, yPixelOffset, xPosition, yPosition):
        super().Render(canvas, xPixelOffset, yPixelOffset, xPosition, yPosition)
        canvas.create_text(self.x + self.width / 2, self.y + self.height / 2, fill="black", font="sans-serif 8", text="!")


class DecorativeTile(SpecialTile):
    fill = "pink"
    width = 16
    height = 16

    changeRoom = None

    def Create(self, changeRoom):
        self.changeRoom = changeRoom

    def DoSpecialAction(self, collision, screenWidth, screenHeight):
        pass

    def Render(self, canvas, xPixelOffset, yPixelOffset, xPosition, yPosition):
        super().Render(canvas, xPixelOffset, yPixelOffset, xPosition, yPosition)



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
            collision[0].xMomentum -= self.boostSpeed 

        if self.boostDirection == 1:
            collision[0].yMomentum -= self.boostSpeed 

        if self.boostDirection == 2:
            collision[0].xMomentum += self.boostSpeed 

        if self.boostDirection == 3:
            collision[0].xMomentum += self.boostSpeed 


    def Render(self, canvas, xPixelOffset, yPixelOffset, xPosition, yPosition):
        super().Render(canvas, xPixelOffset, yPixelOffset, xPosition, yPosition)
        canvas.create_text(self.x + self.width / 2, self.y + self.height / 2, fill="black", font="sans-serif 8", text=self.text)

