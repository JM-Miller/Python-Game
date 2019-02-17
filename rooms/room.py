class Room():

    gameObjects = []
    
    def Render(self, canvas):
        for gameObject in self.gameObjects:
            gameObject.Render(canvas)

        
    def Update(self, keysHeld):
        for gameObject in self.gameObjects:
            gameObject.Update(keysHeld)


    def Create(self):
        for gameObject in self.gameObjects:
            gameObject.Create()


    def Destroy(self):
        pass