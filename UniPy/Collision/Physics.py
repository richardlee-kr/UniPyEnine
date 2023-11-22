from ..Vector import *

#TODO Overlap Physics
class Physics:
    def __init__(self, targetScene):
        self.scene = targetScene

    '''
    Add all objects which have Collider in Scene to list
    Check if item in list is overlapped
    Add overlapped item to list
    Return list
    '''

    def OverlapCircleAll(self, point, radius, layer="Default"):
        allObjects = self.scene.hierarchy
        layered = list()
        detected = list()
        for object in allObjects:
            if object.layer == layer:
                if (object.transform.position - point).magnitude < 2*radius:
                    layered.append(object)
        
        del allObjects

        for object in layered:
            try:
                #if obejct has CircleCollider
                _radius = object.GetComponent("CircleCollider").radius
                _pos = object.GetComponent("CircleCollider").bounds.center + object.transform.position
                if (point-_pos).magnitude <= radius+_radius:
                    detected.append(object)
            except:
                try:
                    # else object has BoxCollider
                    pass
                except:
                    continue

        return detected

    def OverlapBoxAll(self, point, size, layer="Default"):
        allObjects = self.scene.hierarchy
        layered = list()
        detected = list()
        for object in allObjects:
            if object.layer == layer:
                layered.append(object)

        del allObjects

        for object in layered:
            try:
                #if obejct has BoxCollider
                objectPos = object.transform.position
                boundSize = object.GetComponent("BoxCollider").bounds.size
                #print(objectPos.x + boundSize.x/2 >= point.x - size/2)
                if (objectPos.x + boundSize.x/2 >= point.x - size/2 and objectPos.x - boundSize.x/2 <= point.x + size/2):
                    if(objectPos.y + boundSize.y/2 >= point.y - size/2 and objectPos.y - boundSize.y/2 <= point.y + size/2):
                        detected.append(object)
            except:
                try:
                    # else object has CircleColldier
                    print("NO")
                    pass
                except:
                    continue

        return detected