from .log_manager import LogManager


class Player:
    def __init__(self, start_x, start_y, name="Player", symbol="\033[31m@\033[0m"):
        self.x = start_x
        self.y = start_y
        self.name = name
        self.symbol = symbol
        self.previous_tile = " "
        self.last_direction = None

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

        self.last_direction = direction
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

    def check_tile_in_front(self, map_manager, target_symbol="*"):
        """
        Prüft, ob sich vor dem Spieler in der letzten Bewegungsrichtung das Zielzeichen befindet.
        """
        if not self.last_direction:
            return False  # Keine Bewegungsrichtung vorhanden

        # Koordinaten vor der letzten Bewegung berechnen
        check_x, check_y = self.x, self.y

        if self.last_direction == 'W':  # Hoch
            check_y -= 1
        elif self.last_direction == 'A':  # Links
            check_x -= 1
        elif self.last_direction == 'S':  # Runter
            check_y += 1
        elif self.last_direction == 'D':  # Rechts
            check_x += 1

        # Überprüfen, ob der Spieler sich am Rand der Karte befindet
        if not map_manager.is_within_bounds(check_x, check_y):
            return False  # Außerhalb der Karte

        # Prüfen, ob das Tile vor dem Spieler das Zielzeichen enthält
        return map_manager.get_tile(check_x, check_y) == target_symbol