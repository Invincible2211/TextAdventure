from config import Config
import  ui.scenes
from ui.scene import Scene


class MapScene(Scene):
    def __init__(self, ui_manager):
        super().__init__(Config.SCENE_WIDTH, Config.SCENE_HEIGHT, "<KARTE>")
        self.ui_manager = ui_manager

    def update(self, new_data):
        self.content = [''.join(row) for row in new_data]
        self.dirty = True

    def refresh(self):
        """
        Aktualisiert den Inhalt der MapScene basierend auf dem aktuellen Zustand des MapManagers.
        """
        self.content = [''.join(row) for row in self.map_manager.get_visible_map()]
