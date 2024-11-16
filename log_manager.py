import log_scene
import ui_manager


class LogManager:



    def __init__(self, max_entries):
        self.logs = []
        self.full_log = []
        self.max_entries = max_entries
        self.scene = None

    def add_entry(self, message):
        """
        Fügt einen neuen Eintrag zum Log hinzu.
        """
        self.logs.append(message)
        if len(self.logs) > self.max_entries:
            self.full_log.append(self.logs.pop(0))
            ui_manager.sub_scene_dirty = True
        if self.scene is not None:
            self.scene.update()

    def get_logs(self):
        """
        Gibt die aktuellen Log-Einträge zurück.
        """
        return self.logs

    def get_full_log(self):
        return self.full_log

    def add_scene(self, scene:log_scene.LogScene):
        self.scene = scene

