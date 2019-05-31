from tkinter import *
from objects import *
from rooms import test_room
from rooms import menu_room
from time import time, sleep

class Application(Frame):

    keysHeld = []

    isRunning = True

    canvasWidth = 320
    canvasHeight = 320

    rooms = []

    activeRoom = None

    def exit(self):
        if self.isRunning:
            self.isRunning = False
        else:
            self.quit()

    def createWidgets(self):
        self.CANVAS = Canvas(self, width=self.canvasWidth, height=self.canvasHeight)
        self.CANVAS.pack()

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def initGame(self):
        for room in self.rooms:
            room.Create()

    def gameLoop(self):
        self.CANVAS.delete("all")
        self.CANVAS.create_rectangle(0, 0, self.canvasWidth, self.canvasHeight, fill="cornflowerblue")
        self.activeRoom.Update(self.keysHeld)
        self.activeRoom.Render(self.CANVAS)
        # for room in self.rooms:
        #     room.Update(self.keysHeld)
        #     room.Render(self.CANVAS)
            
        self.CANVAS.update()
        
        
    def initGame(self):
        self.activeRoom = test_room.TestRoom()
        self.rooms = { 1: self.activeRoom, 0: menu_room.MenuRoom()}

        for roomIndex in self.rooms:
            self.rooms[roomIndex].Create(self.changeRoom)

    def updateKeysPressed(self, keycode, isPressed):
        if isPressed:
            if keycode not in self.keysHeld:
                self.keysHeld.append(keycode)
        else:
            self.keysHeld.remove(keycode)

    def changeRoom(self, roomId):
        self.activeRoom = self.rooms[roomId] 


root = Tk()
app = Application(master=root)
app.initGame()


root.bind( '<KeyPress>', lambda e: app.updateKeysPressed(e.keycode, True))
root.bind( '<KeyRelease>', lambda e:  app.updateKeysPressed(e.keycode, False))

while app.isRunning:

    fps=60
    frameperiod=1.0/fps
    now=time()
    nextframe=now+frameperiod
    for frame in range(120):
        while now<nextframe:
            sleep(nextframe-now)
            now = time()

    nextframe += frameperiod

    app.gameLoop()
    app.update_idletasks()
    app.update()

root.destroy()