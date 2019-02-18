from objects.tilemap.tile import EmptyTile, SolidTile, WinTile
from objects.game_object import GameObject
from objects.enemies.enemy import Enemy
from csv import *

class TileMap(GameObject):

    x = 0
    y = 0

    mapScrollBuffer = 64

    block = False

    playerObject = None
    tileGrid = []
    tileObjects = []

    gameObjects = []

    def LoadTileMapFile(self, filePath="tilemap.CSV"):
        with open(filePath, 'rt') as mapFile:
            for row in reader(mapFile):
                tileRow = []
                for cell in row:
                    tileRow.append(int(cell))
                self.tileGrid.append(tileRow)

    def LoadTestTileMap(self):
        self.tileGrid = [
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],            
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],            
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],            
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],            
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],            
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],            
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1],            
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],            
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1],            
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],        
            ]
        

    def GetTileByTypeId(self, typeId):
        tileTypes = {
            0: EmptyTile,
            1: SolidTile,
            2: WinTile
        }
        return tileTypes[typeId]()


    def InitializeTiles(self, changeRoom):
        self.tileObjects = []
        for tileRow in self.tileGrid:
            tileObjectRow = []
            for tile in tileRow:
                tileOfType = self.GetTileByTypeId(tile)
                tileOfType.Create(changeRoom)
                tileObjectRow.append(tileOfType)
            self.tileObjects.append(tileObjectRow)

    def Create(self, changeRoom, player, scrollBuffer):


        testEnemy = Enemy()
        testEnemy.Create(self.playerObject)
        self.gameObjects.append(testEnemy)

        # self.LoadTestTileMap()
        self.LoadTileMapFile()
        self.InitializeTiles(changeRoom)
        self.playerObject = player
        self.mapScrollBuffer = scrollBuffer

    def Update(self, keysHeld, screenWidth, screenHeight, collisionObjects):
        if self.playerObject.yTileMapMove != 0:
            self.y = -self.playerObject.yTileMapMove

        if self.playerObject.xTileMapMove != 0:
            self.x = -self.playerObject.xTileMapMove
        
        collisions = [self.playerObject]

        for tileObjectRow in self.tileObjects:
            for tile in tileObjectRow:
                if tile.block:
                    collisions.append(tile)
                if tile.special:
                    tile.Update(self, keysHeld, collisionObjects=[self.playerObject])

                    
        for gameObject in self.gameObjects:
            gameObject.Update(keysHeld, self.x, self.y, screenWidth, screenHeight, collisions)


    def Render(self, canvas):

        for tileObjectRow in self.tileObjects:
            for tile in tileObjectRow:
                tile.Render(canvas, self.x, self.y, tileObjectRow.index(tile), self.tileObjects.index(tileObjectRow))