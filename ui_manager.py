import os

import ui_manager
from config import Config

# Flags für geänderte Bereiche
scene_dirty = True
actions_dirty = True
sub_scene_dirty = True

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def move_cursor_to_position(x, y):
    """
    Bewegt den Cursor an die Position (x, y) im Terminal.
    """
    print(f"\033[{y};{x}H", end="")


def set_scene_dirty():
    ui_manager.scene_dirty =True


def set_sub_scene_dirty():
    ui_manager.sub_scene_dirty =True


def set_actions_dirty():
    ui_manager.actions_dirty =True


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

        if ui_manager.scene_dirty:
            self.render_scene(scene)
            ui_manager.scene_dirty = False
        if ui_manager.actions_dirty:
            self.render_actions(actions)
            ui_manager.actions_dirty = False
        if ui_manager.sub_scene_dirty:
            self.render_sub_scene(sub_scene, actions)
            ui_manager.sub_scene_dirty =False

    def render_scene(self, scene):
        """
        Rendert eine allgemeine Szene innerhalb der Karten-Border.
        """
        move_cursor_to_position(1, 1)
        print(" " * self.padding + f"╔{str(scene.get_title()).center(self.scene_width,"═")}╗")
        for i in range(self.scene_height):
            scene_line = scene.get_line(i)
            print(" " * self.padding + f"║{scene_line}║")
        print(" " * self.padding + f"╚{'═' * self.scene_width}╝")

    def render_actions(self, actions):

        move_cursor_to_position(1, self.scene_height + 3)

        # Aktionen rendern
        print(" " * self.padding + f"╔{'<AKTIONEN>'.center(self.scene_width, "═")}╗")

        for i in range(Config.ACTIONS_HEIGHT):
            if i < len(actions):
                # Leerzeichen nach ║ einfügen
                action_text = actions[i][:self.scene_width - 3]
                print(f" " * self.padding + f"║ {action_text.ljust(self.scene_width - 2)} ║")
            else:
                # Leere Zeilen für fehlende Aktionen
                print(f" " * self.padding + f"║ {' ' * (self.scene_width - 2)} ║")

        print(" " * self.padding + f"╚{'═' * self.scene_width}╝")

    def render_sub_scene(self, sub_scene, actions):
        # Log-Border oben
        move_cursor_to_position(self.scene_width + 2 * self.padding + 1, 1)
        print(f"╔{str(sub_scene.get_title()).center(self.sub_scene_width,'═')}╗")
        for i in range(self.sub_scene_height):
            sub_scene_content = "" + sub_scene.get_line(i)
            sub_scene_line = sub_scene_content if len(sub_scene_content) == self.sub_scene_width else " " + sub_scene_content
            move_cursor_to_position(self.scene_width + 2 * self.padding + 1, i + 2)
            print(f"║{sub_scene_line.ljust(self.sub_scene_width)}║")
        # sub scene border unten
        move_cursor_to_position(self.scene_width + 2 * self.padding + 1, self.sub_scene_height + 2)
        print(f"╚{'═' * self.sub_scene_width}╝")