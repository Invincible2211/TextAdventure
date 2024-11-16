import os

from config import Config


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

    def render(self, scene, log_manager, actions):
        """
        Zeichnet die Benutzeroberfläche. Map, Aktionen und Log werden unabhängig gerendert.
        """
        clear_screen()
        self.render_scene(scene)
        self.render_actions(actions)
        self.render_log(log_manager, actions)

    def render_scene(self, scene):
        """
        Rendert eine allgemeine Szene innerhalb der Karten-Border.
        """
        move_cursor_to_position(1, 1)
        print(" " * self.padding + f"╔{'═' * self.scene_width}╗")
        for i in range(self.scene_height):
            scene_line = scene.get_line(i)
            print(" " * self.padding + f"║{scene_line}║")
        print(" " * self.padding + f"╚{'═' * self.scene_width}╝")

    def render_map(self, map_manager):
        """
        Rendert die Karte und darunter die Aktionen.
        """
        # Karte rendern
        move_cursor_to_position(1, 1)
        print(" " * self.padding + f"╔{'═' * self.scene_width}╗")
        for i in range(self.scene_height):
            map_line = ''.join(map_manager.map_data[i])
            print(" " * self.padding + f"║{map_line}║")
        print(" " * self.padding + f"╚{'═' * self.scene_width}╝")

    def render_actions(self, actions):
        # Aktionen rendern
        print(" " * self.padding + f"╔{'═' * self.scene_width}╗")

        for i in range(Config.ACTIONS_HEIGHT):
            if i < len(actions):
                # Leerzeichen nach ║ einfügen
                action_text = actions[i][:self.scene_width - 3]
                print(f" " * self.padding + f"║ {action_text.ljust(self.scene_width - 2)} ║")
            else:
                # Leere Zeilen für fehlende Aktionen
                print(f" " * self.padding + f"║ {' ' * (self.scene_width - 2)} ║")

        print(" " * self.padding + f"╚{'═' * self.scene_width}╝")

    def render_log(self, log_manager, actions):
        """
        Rendert den Log rechts neben der Karte und den Aktionen.
        """
        # Log-Border oben
        move_cursor_to_position(self.scene_width + 2 * self.padding + 1, 1)
        print(f"╔{'═' * self.sub_scene_width}╗")

        # Log-Inhalt
        for i in range(self.sub_scene_height):
            log_line = self._get_log_line(i, log_manager)
            move_cursor_to_position(self.scene_width + 2 * self.padding + 1, i + 2)
            print(f"║{log_line}║")

        # Log-Border unten
        move_cursor_to_position(self.scene_width + 2 * self.padding + 1, self.sub_scene_height + 2)
        print(f"╚{'═' * self.sub_scene_width}╝")

    def _get_log_line(self, index, log_manager):
        """
        Holt die Log-Zeile für einen bestimmten Index, falls vorhanden, sonst eine leere Zeile.
        """
        if index < len(log_manager.logs):
            return (" " + log_manager.logs[index]).ljust(self.sub_scene_width)
        return " " * self.sub_scene_width