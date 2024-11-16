from Scene import Scene


class MapScene(Scene):
    def __init__(self, map_manager):
        super().__init__(map_manager.width, map_manager.height)
        self.map_manager = map_manager

    def refresh(self):
        """
        Aktualisiert den Inhalt der MapScene basierend auf dem aktuellen Zustand des MapManagers.
        """
        self.content = [''.join(row) for row in self.map_manager.get_visible_map()]
