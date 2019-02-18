from objects.game_object import GameObject

class SolidTile(GameObject):

    width = 17
    height = 17
    weight = 0
    xOrigin = 0
    yOrigin = 0
    fill = "black"

    
    def Render(self, canvas, xPixelOffset, yPixelOffset, xPosition, yPosition):

        self.x = xPosition * self.width + xPixelOffset
        self.y = yPosition * self.height + yPixelOffset

        canvas.create_rectangle(self.x, self.y, self.width + self.x, self.height + self.y, fill=self.fill)

class EmptyTile(GameObject):

    width = 16
    height = 16
    weight = 0
    xOrigin = 0
    yOrigin = 0
    fill = "white"
    block = False

    
    def Render(self, canvas, xPixelOffset, yPixelOffset, xPosition, yPosition):
        pass
        # self.x = yPosition * self.width
        # self.y = xPosition * self.height

        # if self.sprite is None:
        # canvas.create_rectangle(self.x, self.y, self.width + self.x, self.height + self.y, fill=self.fill)
        # else:
        #     canvas.create_image(self.x, self.y, self.width + self.x, self.height + self.y, image=self.sprite)