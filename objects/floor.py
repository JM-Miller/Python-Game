from objects.game_object import GameObject

class Floor(GameObject):

    x = 0
    y = 288
    width = 180
    height = 32
    weight = 0
    sprite = None
    fill = "black"

    
    def Render(self, canvas):
        canvas.create_rectangle(self.x, self.y, self.width + self.x, self.height + self.y, fill=self.fill)