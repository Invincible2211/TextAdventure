from src.config import Config
from src.ui.scene import Scene
from src.ui.utils.text_utils import center_text_in_bounds


class MainMenuScene(Scene):
    def __init__(self):
        super().__init__(Config.SCENE_WIDTH, Config.SCENE_HEIGHT, "<HAUPTMENÜ>")
        self.content = center_text_in_bounds(Config.TITLE, Config.SUB_SCENE_WIDTH, Config.SCENE_HEIGHT)
