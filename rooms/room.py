class Room():

    gameObjects = []
    tileMaps = []
    activeUpdate = False
    activeRender = False
    arg = None
    
    def Render(self, canvas):
        for gameObject in self.gameObjects:
            gameObject.Render(canvas)
        for tileMap in self.tileMaps:
            for gameObject in tileMap.gameObjects:
                gameObject.Render(canvas)


        
    def Update(self, keysHeld):
        for gameObject in self.gameObjects:
            gameObject.Update(keysHeld)
        for tileMap in self.tileMaps:
            for gameObject in tileMap.gameObjects:
                gameObject.Update(keysHeld)


    def Create(self, changeRoom):
        for gameObject in self.gameObjects:
            gameObject.Create(changeRoom)
        for tileMap in self.tileMaps:
            for gameObject in tileMap.gameObjects:
                gameObject.Create(changeRoom)


    def Destroy(self):
        pass