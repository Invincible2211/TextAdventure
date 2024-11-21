from config import Config
from ui.scene import Scene


class FightScene(Scene):
    def __init__(self):
        super().__init__(Config.SCENE_WIDTH, Config.SCENE_HEIGHT, "<KAMPF>")