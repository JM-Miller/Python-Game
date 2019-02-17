from objects.game_object import GameObject

class Platform(GameObject):

    x = 212
    y = 256
    width = 64
    height = 32
    weight = 0
    sprite = None
    fill = "black"

    
    def Render(self, canvas):
        canvas.create_rectangle(self.x, self.y, self.width + self.x, self.height + self.y, fill=self.fill)