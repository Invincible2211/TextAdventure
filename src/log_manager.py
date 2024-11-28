from observable import Observable

class LogManager(Observable):
    logs = []
    full_log = []
    max_entries = 0

    def __init__(self, max_entries):
        super().__init__()
        LogManager.max_entries = max_entries

    @staticmethod
    def add_entry(message):
        """
        Fügt einen neuen Eintrag zum Log hinzu und benachrichtigt alle Observer.
        """
        # Wir greifen direkt auf die statischen Log-Listen zu
        LogManager.logs.append(message)
        if len(LogManager.logs) > LogManager.max_entries:
            LogManager.full_log.append(LogManager.logs.pop(0))

        # Benachrichtige alle Observer (Beobachter) über die Änderung der Logs
        # Hier wird eine Instanz von LogManager benötigt, um die Benachrichtigung zu senden
        if hasattr(LogManager, 'instance') and LogManager.instance:
            LogManager.instance.notify_observers()

    @staticmethod
    def get_logs():
        """
        Gibt die aktuellen Log-Einträge zurück.
        """
        return LogManager.logs

    @staticmethod
    def get_full_log():
        """
        Gibt alle Logs zurück.
        """
        return LogManager.full_log

    @staticmethod
    def set_instance(instance):
        """
        Setzt eine Instanz von LogManager, die für das Benachrichtigen von Beobachtern verwendet wird.
        """
        LogManager.instance = instance
