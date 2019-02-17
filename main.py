from tkinter import *
from objects import *
from rooms import test_room
import msvcrt

class Application(Frame):

    keysHeld = []

    isRunning = True

    canvasWidth = 320
    canvasHeight = 320

    rooms = []

    def exit(self):
        if self.isRunning:
            self.isRunning = False
        else:
            self.quit()

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "Quit"
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.exit
        self.QUIT.pack({"side": "left"})

        self.CANVAS = Canvas(self, width=self.canvasWidth, height=self.canvasHeight)
        self.CANVAS.pack()
        self.CANVAS.create_rectangle(0, 0, self.canvasWidth, self.canvasHeight, fill="cornflowerblue")

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def initGame(self):
        for room in self.rooms:
            room.Create()

    def gameLoop(self):
        self.CANVAS.create_rectangle(0, 0, self.canvasWidth, self.canvasHeight, fill="cornflowerblue")
        for room in self.rooms:
            room.Update(self.keysHeld)
            room.Render(self.CANVAS)
            
        self.CANVAS.update()
        
        
    def initGame(self):
        self.rooms = [test_room.TestRoom()]

        for room in self.rooms:
            room.Create()

    def updateKeysPressed(self, keycode, isPressed):
        if isPressed:
            if keycode not in self.keysHeld:
                self.keysHeld.append(keycode)
        else:
            self.keysHeld.remove(keycode)


root = Tk()
app = Application(master=root)
app.initGame()


root.bind( '<KeyPress>', lambda e: app.updateKeysPressed(e.keycode, True))
root.bind( '<KeyRelease>', lambda e:  app.updateKeysPressed(e.keycode, False))

while app.isRunning:
    app.gameLoop()
    app.update_idletasks()
    app.update()
root.destroy()