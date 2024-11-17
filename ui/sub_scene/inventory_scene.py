from ui.scene import Scene
from config import Config


class InventoryScene(Scene):
    def __init__(self):
        super().__init__(Config.SUB_SCENE_WIDTH, Config.SUB_SCENE_HEIGHT, "<INVENTAR>")
        self.dirty = True

    def update(self, data):
        self.content = [''.join(row) for row in data]
        self.dirty = True