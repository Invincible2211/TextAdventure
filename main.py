from map_manager import MapManager
from player import Player
from log_manager import LogManager
from ui_manager import UIManager

def main():
    # Konstanten
    MAP_WIDTH = 150
    MAP_HEIGHT = 44
    LOG_WIDTH = 50
    PADDING = 2
    MAX_LOG_ENTRIES = MAP_HEIGHT + 6
    ACTIONS = [
        "Aktionen:",
        "[W] Hoch, [A] Links, [S] Runter, [D] Rechts",
        "[I] Inventar, [O] Optionen",
        "Drücke 'Q' zum Beenden."
    ]

    # Initialisierung
    map_manager = MapManager(MAP_WIDTH, MAP_HEIGHT, ".")
    map_manager.load_map_from_file("map.txt")

    player = Player(MAP_WIDTH // 2, MAP_HEIGHT // 2)
    map_manager.update_tile(player.x, player.y, player.symbol)

    log_manager = LogManager(MAX_LOG_ENTRIES)
    log_manager.add_entry("Spiel gestartet.")

    ui_manager = UIManager(MAP_WIDTH, MAP_HEIGHT, LOG_WIDTH, PADDING)

    while True:
        ui_manager.render(map_manager, player, log_manager, ACTIONS)
        action = input("Aktion: ").upper()

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
