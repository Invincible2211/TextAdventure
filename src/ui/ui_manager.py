import os
import re

from config import Config

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def move_cursor_to_position(x, y):
    """
    Bewegt den Cursor an die Position (x, y) im Terminal.
    """
    print(f"\033[{y};{x}H", end="")

# Funktion, um die Länge der ANSI-Sequenzen zu berechnen
def count_ansi_length(text):
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return sum(len(seq) for seq in ansi_escape.findall(text))


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
        title = "" + scene.get_title()
        print(" " * self.padding + f"╔{title.center(self.scene_width + count_ansi_length(title),'═')}╗")
        for i in range(self.scene_height):
            scene_line = "" + scene.get_line(i)
            print(" " * self.padding + f"║{scene_line.ljust(self.scene_width + count_ansi_length(scene_line))}║")
        print(" " * self.padding + f"╚{'═' * self.scene_width}╝")

    def render_actions(self, actions):

        move_cursor_to_position(1, self.scene_height + 3)

        # Aktionen rendern
        print(" " * self.padding + f"╔{'<AKTIONEN>'.center(self.scene_width, '═')}╗")

        for i in range(Config.ACTIONS_HEIGHT):
            action_text = actions.get_line(i)[:self.scene_width - 3]
            print(
                f" " * self.padding + f"║ {action_text.ljust(self.scene_width - 2 + count_ansi_length(action_text))} ║")

        print(" " * self.padding + f"╚{'═' * self.scene_width}╝")

    def render_sub_scene(self, sub_scene, actions):
        # Log-Border oben
        move_cursor_to_position(self.scene_width + 2 * self.padding + 1, 1)
        title = "" + sub_scene.get_title()
        print(f"╔{title.center(self.sub_scene_width + count_ansi_length(title),'═')}╗")
        for i in range(self.sub_scene_height):
            sub_scene_content = "" + sub_scene.get_line(i)
            sub_scene_line = sub_scene_content if len(sub_scene_content) + count_ansi_length(sub_scene_content) == self.sub_scene_width else " " + sub_scene_content
            move_cursor_to_position(self.scene_width + 2 * self.padding + 1, i + 2)
            print(f"║{sub_scene_line.ljust(self.sub_scene_width + count_ansi_length(sub_scene_line))}║")
        # sub scene border unten
        move_cursor_to_position(self.scene_width + 2 * self.padding + 1, self.sub_scene_height + 2)
        print(f"╚{'═' * self.sub_scene_width}╝")