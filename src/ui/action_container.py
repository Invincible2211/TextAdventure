from src.config import Config
from src.ui.scene import Scene

class ActionContainer(Scene):
    def __init__(self):
        super().__init__(Config.SCENE_WIDTH, Config.ACTIONS_HEIGHT)
        self.dirty = True
        self.content = Config.MAP_ACTIONS

    def set_actions(self, actions):
        self.content = actions
        self.dirty = True