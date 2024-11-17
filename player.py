from log_manager import LogManager


class Player:
    def __init__(self, start_x, start_y, name="Player", symbol="\033[31m@\033[0m"):
        self.x = start_x
        self.y = start_y
        self.name = name
        self.symbol = symbol
        self.previous_tile = " "

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

        # Erlaubte Tiles
        allowed_tiles = [" ", "#"]

        # Bewegung prüfen
        if map_manager.get_tile(new_x, new_y) in allowed_tiles:
            # Das aktuelle Tile speichern, bevor der Spieler sich bewegt
            map_manager.update_tile(self.x, self.y, self.previous_tile)  # Altes Feld wiederherstellen
            self.previous_tile = map_manager.get_tile(new_x, new_y)  # Neues Feld speichern
            map_manager.update_tile(new_x, new_y, self.symbol)  # Spieler auf neues Feld setzen
            self.x, self.y = new_x, new_y
            # Karte scrollen, damit der Spieler immer in der Mitte bleibt
            map_manager.scroll_to_position(self.x, self.y)
            LogManager.add_entry(f"\033[31m{self.name}\033[0m bewegte sich nach {direction}.")
            return True
        return False
