import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def move_cursor_to_position(x, y):
    """
    Bewegt den Cursor an die Position (x, y) im Terminal.
    """
    print(f"\033[{y};{x}H", end="")


class UIManager:
    def __init__(self, scene_width, scene_height, sub_scene_width, padding):
        self.scene_width = scene_width
        self.scene_height = scene_height
        self.sub_scene_width = sub_scene_width
        self.padding = padding

    def render(self, map_manager, log_manager, actions):
        """
        Zeichnet die Benutzeroberfläche. Map, Aktionen und Log werden unabhängig gerendert.
        """
        clear_screen()
        self.render_map(map_manager)
        self.render_actions(actions)
        self.render_log(log_manager, actions)

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
        for action in actions:
            print(" " * self.padding + f"║{action.ljust(self.scene_width)}║")
        print(" " * self.padding + f"╚{'═' * self.scene_width}╝")

    def render_log(self, log_manager, actions):
        """
        Rendert den Log rechts neben der Karte und den Aktionen.
        """
        # Log-Border oben
        move_cursor_to_position(self.scene_width + 2 * self.padding + 1, 1)
        print(f"╔{'═' * self.sub_scene_width}╗")

        # Log-Inhalt
        log_height = self.scene_height + len(actions) + 2  # Map-Höhe + Aktionen + Border
        for i in range(log_height):
            log_line = self._get_log_line(i, log_manager)
            move_cursor_to_position(self.scene_width + 2 * self.padding + 1, i + 2)
            print(f"║{log_line}║")

        # Log-Border unten
        move_cursor_to_position(self.scene_width + 2 * self.padding + 1, log_height + 2)
        print(f"╚{'═' * self.sub_scene_width}╝")

    def _get_log_line(self, index, log_manager):
        """
        Holt die Log-Zeile für einen bestimmten Index, falls vorhanden, sonst eine leere Zeile.
        """
        if index < len(log_manager.logs):
            return (" " + log_manager.logs[index]).ljust(self.sub_scene_width)
        return " " * self.sub_scene_width