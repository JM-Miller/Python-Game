from objects.tilemap.tilemap import TileMap
from objects.player import Player
from rooms.room import Room

class TestRoom(Room):

    gravity = 1
    tileMaps = []
    collisionObjectsInRoom = []

    def Create(self):
        foregroundTileMap = TileMap()
        self.tileMaps = [foregroundTileMap]
        self.gameObjects = [foregroundTileMap, Player()]
        for gameObject in self.gameObjects:
            gameObject.Create()

        for tileMap in self.tileMaps:
            for tileRow in tileMap.tileObjects:
                for tileObject in tileRow:
                    if tileObject.block:
                        self.collisionObjectsInRoom.append(tileObject)
                        
        for gameObject in self.gameObjects:
            if gameObject.block:
                self.collisionObjectsInRoom.append(gameObject)


    def Update(self, keysHeld):

        for gameObject in self.gameObjects:
            yAdd = self.gravity * gameObject.weight
            gameObject.yMomentum += yAdd
            
            gameObject.Update(keysHeld, self.collisionObjectsInRoom)

