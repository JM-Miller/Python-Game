class Room():

    gameObjects = []
    
    def Render(self, canvas):
        for gameObject in self.gameObjects:
            gameObject.Render(canvas)

        
    def Update(self, keysHeld):
        for gameObject in self.gameObjects:
            gameObject.Update(keysHeld)


    def Create(self, changeRoom):
        for gameObject in self.gameObjects:
            gameObject.Create(changeRoom)


    def Destroy(self):
        pass