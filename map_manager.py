from config import Config
from observable import Observable


class MapManager(Observable):
    def __init__(self, fill_char=" "):
        super().__init__()
        self.width = Config.SCENE_WIDTH
        self.height = Config.SCENE_HEIGHT
        self.fill_char = fill_char
        self.map_data = []
        self.scroll_x = 0
        self.scroll_y = 0

    def load_map_from_file(self, filename):
        """
        Lädt die Karte aus einer Datei und passt sie an die gewünschte Größe an.
        """
        map_data = []
        max_width = 0  # Variable zur Speicherung der maximalen Zeilenbreite

        # Zuerst die Datei lesen und gleichzeitig die maximale Zeilenbreite ermitteln
        with open(filename, 'r') as file:
            for line in file.readlines():
                line = line.rstrip()  # Entfernen von trailing Whitespace
                max_width = max(max_width, len(line))  # Update der maximalen Breite
                map_data.append(list(line))  # Zeile zur Karte hinzufügen

        # Fülle die Zeilen auf die maximale Breite auf
        for i in range(len(map_data)):
            map_data[i] = map_data[i] + [self.fill_char] * (max_width - len(map_data[i]))

        # Füge leere Zeilen hinzu, wenn die Karte nicht genug Zeilen hat
        while len(map_data) < self.height:
            map_data.append([self.fill_char] * max_width)

        self.map_data = map_data

    def update_tile(self, x, y, char):
        """
        Aktualisiert ein Feld in der Karte.
        """
        if 0 <= y < len(self.map_data) and 0 <= x < len(self.map_data[0]):
            self.map_data[y][x] = char
            self.notify_observers(self.get_visible_map())

    def get_tile(self, x, y):
        """
        Gibt das Zeichen an einer bestimmten Position zurück.
        """
        if 0 <= y < len(self.map_data) and 0 <= x < len(self.map_data[0]):
            return self.map_data[y][x]
        return None

    def scroll_to_position(self, player_x, player_y):
        """
        Scrollt die Karte, sodass der Spieler immer in der Mitte bleibt,
        solange er sich nicht zu nah an einem Rand befindet.
        """
        if player_x - self.scroll_x < self.width // 2:
            self.scroll_x = max(0, player_x - self.width // 2)
        elif player_x - self.scroll_x > self.width // 2:
            self.scroll_x = min(len(self.map_data[0]) - self.width, player_x - self.width // 2)

        if player_y - self.scroll_y < self.height // 2:
            self.scroll_y = max(0, player_y - self.height // 2)
        elif player_y - self.scroll_y > self.height // 2:
            self.scroll_y = min(len(self.map_data) - self.height, player_y - self.height // 2)
        self.notify_observers(self.get_visible_map())

    def get_visible_map(self):
        """
        Gibt einen Ausschnitt der Karte zurück, der dem aktuellen Scrollbereich entspricht.
        """
        visible_map = []

        for y in range(self.scroll_y, min(self.scroll_y + self.height, len(self.map_data))):
            # Berechne den sichtbaren Ausschnitt der aktuellen Zeile
            row = self.map_data[y][self.scroll_x:self.scroll_x + self.width]

            # Fülle die Zeile auf, wenn sie nicht lang genug ist
            if len(row) < self.width:
                row += [self.fill_char] * (self.width - len(row))  # Füge Leerräume am Ende hinzu

            visible_map.append(row)

        # Falls die sichtbare Map in vertikaler Richtung zu wenig Zeilen hat, fülle mit leeren Zeilen auf
        while len(visible_map) < self.height:
            visible_map.append([self.fill_char] * self.width)

        return visible_map
