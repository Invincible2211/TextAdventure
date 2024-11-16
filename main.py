from map_manager import MapManager
from player import Player
from log_manager import LogManager
from ui_manager import UIManager

def main():
    # Konstanten
    SCENE_WIDTH = 150
    SCENE_HEIGHT = 44
    SUB_SCENE_WIDTH = 50
    PADDING = 3
    MAX_LOG_ENTRIES = SCENE_HEIGHT + 6
    ACTIONS = [
        "Aktionen:",
        "[W] Hoch, [A] Links, [S] Runter, [D] Rechts",
        "[I] Inventar, [O] Optionen",
        "Drücke 'Q' zum Beenden."
    ]
    TITLE = [
        "  ___              _  _                          ",
        " / _ \\            (_)(_)                         ",
        "/ /_\\ \\ ___   ___  _  _  _ __ ___    ___   _ __  ",
        "|  _  |/ __| / __|| || || '_ ` _ \\  / _ \\ | '_ \\ ",
        "| | | |\\__ \\| (__ | || || | | | | || (_) || | | |",
        "\\_| |_/|___/ \\___||_||_||_| |_| |_| \\___/ |_| |_|"
    ]

    # Initialisierung
    map_manager = MapManager(SCENE_WIDTH, SCENE_HEIGHT, " ")
    map_manager.load_map_from_file("map.txt")

    player = Player(SCENE_WIDTH // 2, SCENE_HEIGHT // 2)
    map_manager.update_tile(player.x, player.y, player.symbol)

    log_manager = LogManager(MAX_LOG_ENTRIES)
    log_manager.add_entry("Spiel gestartet.")

    ui_manager = UIManager(SCENE_WIDTH, SCENE_HEIGHT, SUB_SCENE_WIDTH, PADDING)

    while True:
        ui_manager.render(map_manager, log_manager, ACTIONS)
        action = input("   Aktion: ").upper()

        if action == "Q":
            log_manager.add_entry("Spiel beendet.")
            break
        elif action in ["W", "A", "S", "D"]:
            if player.move(action, map_manager):
                log_manager.add_entry(f"Spieler bewegte sich nach {action}.")
            else:
                log_manager.add_entry(f"Bewegung nach {action} blockiert.")
        elif action == "I":
            log_manager.add_entry("Inventar geöffnet.")
        elif action == "O":
            log_manager.add_entry("Optionen geöffnet.")
        else:
            log_manager.add_entry("Ungültige Eingabe.")

if __name__ == "__main__":
    main()
