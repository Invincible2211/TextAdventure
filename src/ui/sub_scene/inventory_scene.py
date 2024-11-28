from src.ui.scene import Scene
from src.config import Config


class InventoryScene(Scene):
    def __init__(self):
        super().__init__(Config.SUB_SCENE_WIDTH, Config.SUB_SCENE_HEIGHT, "<INVENTAR>")
        self.dirty = True

    def update(self, data, cursor):
        self.content = []

        for i, item in enumerate(data):
            if i == cursor:
                self.content.append(f"> {item}")  # Cursor-Hinweis
            else:
                self.content.append(f"  {item}")  # Standard-Offset

        self.dirty = True