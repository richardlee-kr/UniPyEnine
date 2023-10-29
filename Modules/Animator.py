from Modules.Component import *

class Animator(Component):
    def __init__(self):
        self.name = "Animator"
        self.entry = None
        self.states = list()
        self.parameters = list()
        self.animations = list()
        self.transitions = list()
        self.currentClip = None
        self.isPlaying = True

    def Play(self): self.isPlaying = True
    def Stop(self): self.isPlaying = False

    def Update(self):
        if self.isPlaying:
            self.currentClip.Play()
