from Scene import Scene
from config import Config


class LogScene(Scene):
    def __init__(self, log_manager):
        super().__init__(Config.SUB_SCENE_WIDTH, Config.SUB_SCENE_HEIGHT, "<LOG>")
        self.log_manager = log_manager

    def update(self):
        self.content = self.log_manager.get_logs()