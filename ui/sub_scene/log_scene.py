from config import Config
from log_manager import LogManager
from ui.scene import Scene


class LogScene(Scene):
    def __init__(self):
        super().__init__(Config.SUB_SCENE_WIDTH, Config.SUB_SCENE_HEIGHT, "<LOG>")
        self.dirty = True

    def update(self):
        self.content = LogManager.get_logs()
        self.dirty = True