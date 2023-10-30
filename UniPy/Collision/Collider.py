from ..Component import *
from ..Vector import *
from .Bound import *

class Collider(Component):
    def __init__(self):
        super(Collider, self).__init__(self)
        self.name = "Collider"
        self.offset = Vector.zero
        self.bounds = Bound(Vector.zero)