from objects.tilemap.tilemap import TileMap
from objects.player import Player
from rooms.room import Room

class DialogRoom(Room):

    screenWidth = 320
    screenHeight = 320

    menuFontSize = 8
    menuFontColor = "white"
    optionFontColor = "gray"

    changeRoom = None
    currentConvo = []
    currentDialog = "Hi! I'm a dialog thing!"
    textOptions = []
    currentDialogIndex = 0
    selectedOptionIndex = 0

    unactiveMaxTime = 10
    unactiveTime = 10


    def Create(self, changeRoom):
        self.changeRoom = changeRoom

    def Update(self, keysHeld):
        if not self.currentConvo:
            self.currentConvo = self.GetDialogText(self.arg)
        if self.currentDialogIndex < len(self.currentConvo):
            textLine = self.currentConvo[self.currentDialogIndex]
            if type(textLine[1]) is str:
                self.currentDialog = textLine      
            if type(textLine[1]) is list:
                self.textOptions = textLine  
        elif self.unactiveTime < 0:
            self.activeRender = True

        # if not 32 in keysHeld:
        if self.unactiveTime < 0:
            if 40 in keysHeld:
                self.unactiveTime = self.unactiveMaxTime
                if self.selectedOptionIndex == len(self.textOptions) - 1:
                    self.selectedOptionIndex = 0
                else:
                    self.selectedOptionIndex += 1
            if 38 in keysHeld:
                self.unactiveTime = self.unactiveMaxTime
                if self.selectedOptionIndex == 0:
                    self.selectedOptionIndex = len(self.textOptions) - 1
                else:
                    self.selectedOptionIndex -= 1

            if 32 in keysHeld:
                self.unactiveTime = self.unactiveMaxTime
                if self.textOptions:
                    self.DoOption(self.currentDialogIndex, self.selectedOptionIndex) 
                else:
                    if self.currentDialogIndex == len(self.currentConvo) - 1:
                        self.activeRender = False
                        self.activeUpdate = False
                        self.currentDialogIndex = 0
                        self.currentConvo = []
                        self.changeRoom(1)
                    else:
                        self.currentDialogIndex += 1
        self.unactiveTime -= 1

    def Render(self, canvas):
        canvas.create_rectangle(0, self.screenHeight - 100, self.screenWidth, self.screenHeight, fill="brown")
        canvas.create_text(16, self.screenHeight - 82, anchor="nw", fill=self.menuFontColor, font="sans-serif " + str(self.menuFontSize), text=self.currentDialog[1])
        canvas.create_rectangle(16, self.screenHeight - 84, 80, self.screenHeight - 148, fill="blue")
        canvas.create_text(24, self.screenHeight - 100, anchor="nw", fill=self.menuFontColor, font="sans-serif " + str(self.menuFontSize), text=self.GetDialogSpeaker(self.currentDialog[0]))
        if self.textOptions:
            for index, textOption in enumerate(self.textOptions):
                color = self.menuFontColor
                if index != self.selectedOptionIndex:
                    color = self.optionFontColor

                canvas.create_text(16, self.screenHeight - 41 + (index * (self.menuFontSize + 2)), anchor="nw", fill=color, font="sans-serif " + str(self.menuFontSize), text=str(textOption[0][1]))

    def DoOption(self, dialogPositionIndex, optionIndex):
        self.textOptions = []
        self.currentConvo = self.currentConvo[dialogPositionIndex][optionIndex]
        self.currentDialogIndex = 0
        self.selectedOptionIndex = 0

    def GetDialogSpeaker(self, speakerId):
        speakers = {
            0: "You",
            1: "The Sign",
            2: "Cave Guy"
        }

        return speakers[speakerId]

    def GetDialogText(self, dialogId):
        dialog = {
            0: [[0, "Ooops a daisy"]],
            1: [[1, "Hey, what's up? I'm a sign."], [1, "Ya know, one of those readable wooden posts?"]],
            2: [
                [2, "Welcome to my cave."],
                [
                    [[0, "What a good cave!"], [2, "Yeah, I know."]], 
                    [[0, "This is MY cave now!!"], [2, "aw... okay."]], 
                ]
            ]
        }
        return dialog[dialogId]

