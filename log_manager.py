class LogManager:
    def __init__(self, max_entries):
        self.logs = []
        self.max_entries = max_entries

    def add_entry(self, message):
        """
        Fügt einen neuen Eintrag zum Log hinzu.
        """
        self.logs.append(message)
        if len(self.logs) > self.max_entries:
            self.logs.pop(0)

    def get_logs(self):
        """
        Gibt die aktuellen Log-Einträge zurück.
        """
        return self.logs
