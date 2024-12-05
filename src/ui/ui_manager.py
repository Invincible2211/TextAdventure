import os

from .utils.frame_generator import frame_text
from ..config import Config


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def move_cursor_to_position(x, y):
    """
    Bewegt den Cursor an die Position (x, y) im Terminal.
    """
    print(f"\033[{y};{x}H", end="")


class UIManager:

    def __init__(self):
        self.scene_width = Config.SCENE_WIDTH
        self.scene_height = Config.SCENE_HEIGHT
        self.sub_scene_width = Config.SUB_SCENE_WIDTH
        self.sub_scene_height = Config.SUB_SCENE_HEIGHT
        self.padding = Config.PADDING
        clear_screen()

    def render(self, scene, sub_scene, actions):
        """
        Zeichnet die Benutzeroberfläche. Map, Aktionen und Log werden unabhängig gerendert.
        """

        if scene.dirty:
            self.render_scene(scene)
            scene.dirty = False
        if actions.dirty:
            self.render_actions(actions)
            actions.dirty = False
        if sub_scene.dirty:
            self.render_sub_scene(sub_scene, actions)
            sub_scene.dirty = False

    def render_scene(self, scene):
        """
        Rendert eine allgemeine Szene innerhalb der Karten-Border.
        """
        move_cursor_to_position(1, 1)
        scene_lines = frame_text(scene, self.scene_width, self.scene_height, scene.get_title())
        for line in scene_lines:
            print(" " * self.padding + line)

    def render_actions(self, actions):
        """
        Rendert die Aktionen im vorgesehenen Bereich.
        """
        move_cursor_to_position(1, self.scene_height + 3)

        action_lines = frame_text(actions, self.scene_width, Config.ACTIONS_HEIGHT, "<AKTIONEN>")
        for line in action_lines:
            print(" " * self.padding + line)

    def render_sub_scene(self, sub_scene, actions):
        """
        Rendert die Sub-Szene mit den entsprechenden Log-Inhalten.
        Achtet darauf, die Zeilen an die richtige Position zu setzen.
        """
        # Holen der gerenderten Zeilen für die Sub-Szene
        sub_scene_lines = frame_text(sub_scene, self.sub_scene_width, self.sub_scene_height, sub_scene.get_title())

        # Startposition für die Sub-Szene
        start_y_position = 1  # Ausgangspunkt für den Y-Cursor

        # Drucken der gerenderten Sub-Szene unter Beachtung der Cursorposition
        for line in sub_scene_lines:
            move_cursor_to_position(self.scene_width + 2 * self.padding + 1, start_y_position)
            print(line)
            start_y_position += 1  # Erhöht die Y-Position für die nächste Zeile
