import os


class UIManager:

    def __init__(self, map_width, map_height, log_width, padding):
        self.map_width = map_width
        self.map_height = map_height
        self.log_width = log_width
        self.padding = padding

    def render(self, map_manager, player, log_manager, actions):
        """
        Zeichnet die Benutzeroberfläche.
        """
        os.system('cls' if os.name == 'nt' else 'clear')

        # Top-Border
        self._print_top_border()

        # Map und Log nebeneinander
        total_log_height = self.map_height + len(actions) + 2  # Höhe von Karte + Aktionen + Border
        for i in range(self.map_height):
            map_line = ''.join(map_manager.map_data[i])
            log_line = self._get_log_line(i, log_manager)
            print(f" " * self.padding + f"║{map_line}║{' ' * self.padding}║{log_line}║")

        # Bottom-Border für Karte und Log
        self._print_bottom_border(log_manager)

        # Aktionen
        self._render_actions(actions, log_manager)

    def _print_top_border(self):
        """
        Druckt die obere Border der Map- und Log-Ansicht.
        """
        print(" " * self.padding + f"╔{'═' * self.map_width}╗{' ' * self.padding}╔{'═' * self.log_width}╗")

    def _print_bottom_border(self, log_manager):
        """
        Druckt die untere Border der Map- und Log-Ansicht sowie die Aktionsfeld-Border.
        """
        log_line = self._get_log_line(self.map_height, log_manager)
        print(" " * self.padding + f"╚{'═' * self.map_width}╝{' ' * self.padding}║{log_line}║")

    def _render_actions(self, actions, log_manager):
        """
        Zeigt das Aktionen-Feld unter der Karte an.
        """
        log_line = self._get_log_line(self.map_height + 1, log_manager)
        print(f" " * self.padding + f"╔{'═' * self.map_width}╗{' ' * self.padding}║{log_line}║")

        for i, action in enumerate(actions, start=2):
            log_line = self._get_log_line(self.map_height + i, log_manager)
            print(f" " * self.padding + f"║{action.ljust(self.map_width)}║{' ' * self.padding}║{log_line}║")

        print(" " * self.padding + f"╚{'═' * self.map_width}╝{' ' * self.padding}╚{'═' * self.log_width}╝")

    def _get_log_line(self, index, log_manager):
        """
        Holt die Log-Zeile für einen bestimmten Index, falls vorhanden, sonst eine leere Zeile.
        """
        return (" " + log_manager.logs[index]).ljust(self.log_width) if index < len(log_manager.logs) else " " * self.log_width