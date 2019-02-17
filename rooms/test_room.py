from objects.floor import Floor
from objects.platform import Platform
from objects.player import Player
from rooms.room import Room

class TestRoom(Room):

    gravity = 1

    def Create(self):
        self.gameObjects = [Floor(), Platform(), Player()]
        for gameObject in self.gameObjects:
            gameObject.Create()

    def Update(self, keysHeld):
        collisionObjectsInRoom = []
        for gameObject in self.gameObjects:
            if gameObject.block:
                collisionObjectsInRoom.append(gameObject)

        for gameObject in self.gameObjects:
            yAdd = self.gravity * gameObject.weight
            gameObject.yMomentum += yAdd
            
            gameObject.Update(keysHeld, collisionObjectsInRoom)

