from objects.tilemap.tilemap import TileMap
from objects.player import Player
from rooms.room import Room

class MenuRoom(Room):

    screenWidth = 320
    screenHeight = 320

    menuFontSize = 24
    menuFontColor = "white"
    

    def Render(self, canvas):
        menuItemText = "You win!"
        canvas.create_rectangle(0, 0, self.screenWidth, self.screenHeight, fill="black")
        
        canvas.create_text(self.screenWidth / 2, self.screenHeight / 2, fill=self.menuFontColor, font="sans-serif " + str(self.menuFontSize), text=menuItemText)