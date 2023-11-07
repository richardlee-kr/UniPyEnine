from .Transform import *

class GameObject:
    def __init__(self, name):
        self.name = name
        self.layer = "Default"
        self.tag = "Untagged"
        self.transform = Transform()
        self.components = list()
        self.AddComponent(self.transform)
    
    def AddComponent(self, cmpnt):
        self.components.append(cmpnt)
        cmpnt.gameObject = self
        cmpnt.transform = self.transform

    def GetComponent(self, cmpnt):
        for item in self.components:
            if cmpnt == item.name:
                return item

    def Update(self):
        pass

    def DestroyFrom(self, scene):
        scene.hierarchy.remove(self)
        del self

    @staticmethod
    def Instantiate(scene, object, pos, rot):
        scene.hierarchy.append(object)
        object.transform.position = pos
        object.transform.Rotate(rot)