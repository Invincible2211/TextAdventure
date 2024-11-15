class MapManager:
    def __init__(self, width, height, fill_char=" "):
        self.width = width
        self.height = height
        self.fill_char = fill_char
        self.map_data = []

    def load_map_from_file(self, filename):
        """
        Lädt die Karte aus einer Datei und passt sie an die gewünschte Größe an.
        """
        map_data = []
        with open(filename, 'r') as file:
            for line in file.readlines():
                adjusted_line = list(line.rstrip().ljust(self.width, self.fill_char))
                map_data.append(adjusted_line)
        while len(map_data) < self.height:
            map_data.append([self.fill_char] * self.width)
        self.map_data = map_data[:self.height]

    def update_tile(self, x, y, char):
        """
        Aktualisiert ein Feld in der Karte.
        """
        if 0 <= y < self.height and 0 <= x < self.width:
            self.map_data[y][x] = char

    def get_tile(self, x, y):
        """
        Gibt das Zeichen an einer bestimmten Position zurück.
        """
        if 0 <= y < self.height and 0 <= x < self.width:
            return self.map_data[y][x]
        return None
