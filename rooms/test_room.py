from objects.tilemap.tilemap import TileMap
from objects.player import Player
from rooms.room import Room

class TestRoom(Room):

    screenWidth = 320
    screenHeight = 320
    
    scrollBuffer = 64

    gravity = 0
    collisionObjectsInRoom = []

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
            for tileRow in tileMap.tileObjects:
                for tileObject in tileRow:
                    if tileObject.block:
                        self.collisionObjectsInRoom.append(tileObject)
                        
        for gameObject in self.gameObjects:
            if gameObject.block:
                self.collisionObjectsInRoom.append(gameObject)


    def Update(self, keysHeld):
        
        for tileMap in self.tileMaps:
            for gameObject in tileMap.gameObjects:
                yAdd = self.gravity * gameObject.weight
                gameObject.yMomentum += yAdd
                gameObject.Update(keysHeld, 0, 0, self.screenWidth, self.screenHeight, self.collisionObjectsInRoom)

        for gameObject in self.gameObjects:
            yAdd = self.gravity * gameObject.weight
            gameObject.yMomentum += yAdd
            gameObject.Update(keysHeld, self.screenWidth, self.screenHeight, self.collisionObjectsInRoom)
