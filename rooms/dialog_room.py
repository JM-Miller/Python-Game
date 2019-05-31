from objects.tilemap.tilemap import TileMap
from objects.player import Player
from rooms.room import Room

class DialogRoom(Room):

    screenWidth = 320
    screenHeight = 320

    menuFontSize = 8
    menuFontColor = "white"

    changeRoom = None

    wasActivateUnheld = False

    def Create(self, changeRoom):
        self.changeRoom = changeRoom

    def Update(self, keysHeld):
        if not 32 in keysHeld:
            self.wasActivateUnheld = True
        if self.wasActivateUnheld and 32 in keysHeld:
            self.wasActivateUnheld = False
            self.activeRender = False
            self.activeUpdate = False
            self.changeRoom(1)

    

    def Render(self, canvas):
        menuItemText = "Hi! I'm a dialog thing!"
        if menuItemText is not None:
            menuItemText = self.GetDialogText(self.arg)
        canvas.create_rectangle(0, self.screenHeight - 100, self.screenWidth, self.screenHeight, fill="brown")
        
        canvas.create_text(72, self.screenHeight - 82, fill=self.menuFontColor, font="sans-serif " + str(self.menuFontSize), text=menuItemText)


    def GetDialogText(self, dialogId):
        dialog = {
            0: "Ooops a daisy",
            1: "Hey, what's up? I'm a sign.",
            2: "Welcome to my cave."
        }
        return dialog[dialogId]

