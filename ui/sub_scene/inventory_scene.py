from ui.scene import Scene
from config import Config


class InventoryScene(Scene):
    def __init__(self, inventory):
        super().__init__(Config.SUB_SCENE_WIDTH, Config.SUB_SCENE_HEIGHT, "<INVENTAR>")
        self.dirty = True
        self.inventory = inventory

    def refresh(self):
        """
        Aktualisiert den Inhalt der MapScene basierend auf dem aktuellen Zustand des MapManagers.
        """
        self.content = [''.join(row) for row in self.inventory.get_items()]
        self.dirty = True
