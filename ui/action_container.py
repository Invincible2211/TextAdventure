from config import Config
from ui.scene import Scene

class ActionContainer(Scene):
    def __init__(self):
        super().__init__(Config.SCENE_WIDTH, Config.ACTIONS_HEIGHT)
        self.dirty = True
        self.content = Config.MAP_ACTIONS