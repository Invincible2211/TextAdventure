import ui_manager


class Player:
    def __init__(self, start_x, start_y, symbol="@"):
        self.x = start_x
        self.y = start_y
        self.symbol = symbol

    def move(self, direction, map_manager):
        """
        Bewegt den Spieler in eine Richtung, falls möglich.
        """
        new_x, new_y = self.x, self.y
        if direction == 'W':  # Hoch
            new_y -= 1
        elif direction == 'A':  # Links
            new_x -= 1
        elif direction == 'S':  # Runter
            new_y += 1
        elif direction == 'D':  # Rechts
            new_x += 1

        # Bewegung prüfen
        if map_manager.get_tile(new_x, new_y) == " ":
            map_manager.update_tile(self.x, self.y, " ")  # Altes Feld freigeben
            map_manager.update_tile(new_x, new_y, self.symbol)  # Neues Feld besetzen
            self.x, self.y = new_x, new_y
            # Karte scrollen, damit der Spieler immer in der Mitte bleibt
            map_manager.scroll_to_position(self.x, self.y)
            return True
        return False
