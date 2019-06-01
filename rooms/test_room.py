from objects.tilemap.tilemap import TileMap
from objects.player import Player
from rooms.room import Room
import time

class TestRoom(Room):

    screenWidth = 320
    screenHeight = 320
    
    scrollBuffer = 64

    gravity = 0
    collisionObjectsInRoom = []

    currentHour = 12
    currentMinute = 0

    lastHitTime = None

    playerObject = None

    def Create(self, changeRoom):
        foregroundTileMap = TileMap()
        self.playerObject = Player()
        self.playerObject.Create(changeRoom, self.scrollBuffer)
        foregroundTileMap.Create(changeRoom, self.playerObject, self.scrollBuffer)

        self.tileMaps = [foregroundTileMap]
        self.gameObjects = [self.playerObject, foregroundTileMap]
        self.gameObjects.append(foregroundTileMap)

        for tileMap in self.tileMaps:
            for gameObject in tileMap.gameObjects:
                if gameObject.block:
                    self.collisionObjectsInRoom.append(gameObject)
            for tileRow in tileMap.tileObjects:
                for tileObject in tileRow:
                    if tileObject.block:
                        self.collisionObjectsInRoom.append(tileObject)
                        
        for gameObject in self.gameObjects:
            if gameObject.block:
                self.collisionObjectsInRoom.append(gameObject)


    def Render(self, canvas):
        super().Render(canvas)
        canvas.create_rectangle(self.screenWidth - 56, 32, self.screenWidth - 16, 56, fill="brown")
        currentMinuteDisplay = str(self.currentMinute)
        if len(currentMinuteDisplay) == 1:
            currentMinuteDisplay = "0" + currentMinuteDisplay
        currentHourDisplay = str(self.currentHour)
        if len(currentHourDisplay) == 1:
            currentHourDisplay = "0" + currentHourDisplay
        canvas.create_text(self.screenWidth - 36, 44, fill="white", font="sans-serif 8", text=(currentHourDisplay + ":" + currentMinuteDisplay))

    def Update(self, keysHeld):

        if not self.lastHitTime:
            self.lastHitTime = time.time()
        else:
            if time.time() - self.lastHitTime > 1:
                self.lastHitTime = time.time()
                self.currentMinute += 1
                if self.currentMinute == 60:
                    self.currentHour += 1
                    self.currentMinute = 0
                    if self.currentHour == 24:
                        self.currentHour = 0
        
        for tileMap in self.tileMaps:
            for gameObject in tileMap.gameObjects:
                yAdd = self.gravity * gameObject.weight
                gameObject.yMomentum += yAdd
                gameObject.Update(keysHeld, self.currentHour, self.currentMinute, self.playerObject.xTileMapMove, self.playerObject.yTileMapMove, screenWidth=self.screenWidth, screenHeight=self.screenHeight, collisionObjects=self.collisionObjectsInRoom)

        for gameObject in self.gameObjects:
            yAdd = self.gravity * gameObject.weight
            gameObject.yMomentum += yAdd
            gameObject.Update(keysHeld, self.currentHour, self.currentMinute, self.playerObject.xTileMapMove, self.playerObject.yTileMapMove, self.screenWidth, self.screenHeight, self.collisionObjectsInRoom, True)
