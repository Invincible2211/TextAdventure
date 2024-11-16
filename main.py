from config import Config
from dialog_scene import DialogScene
from map_manager import MapManager
from map_scene import MapScene
from player import Player
from log_manager import LogManager
from ui_manager import UIManager

def main():
    # Initialisierung
    map_manager = MapManager(" ")
    map_manager.load_map_from_file("map.txt")

    map_manager.load_map_from_file("map.txt")

    player = Player(Config.SCENE_WIDTH // 2, Config.SCENE_HEIGHT // 2)
    map_manager.update_tile(player.x, player.y, player.symbol)

    map_scene = MapScene(map_manager)
    map_scene.refresh()

    log_manager = LogManager(Config.MAX_LOG_ENTRIES)
    log_manager.add_entry("Spiel gestartet.")

    ui_manager = UIManager()

    while True:
        ui_manager.render(map_scene, log_manager, Config.MAP_ACTIONS)
        action = input("   Aktion: ").upper()

        if action == "Q":
            log_manager.add_entry("Spiel beendet.")
            break
        elif action in ["W", "A", "S", "D"]:
            if player.move(action, map_manager):
                map_scene.refresh()
                log_manager.add_entry(f"Spieler bewegte sich nach {action}.")
            else:
                log_manager.add_entry(f"Bewegung nach {action} blockiert.")
        elif action == "I":
            log_manager.add_entry("Inventar geöffnet.")
            # DialogScene initialisieren
            dialog_lines = [
                " INVENTAR:",
                " 1. Heiltrank",
                " 2. Schwert",
                " 3. Schild",
            ]
            dialog_scene = DialogScene(Config.SCENE_WIDTH, Config.SCENE_HEIGHT, dialog_lines)

            # Dialog anzeigen
            while True:
                ui_manager.render(dialog_scene, log_manager, Config.INVENTORY_ACTIONS)
                dialog_action = input("   Dialog Aktion: ").upper()
                if dialog_action == "B":
                    log_manager.add_entry("Inventar geschlossen.")
                    break
        elif action == "O":
            log_manager.add_entry("Optionen geöffnet.")
        else:
            log_manager.add_entry("Ungültige Eingabe.")

if __name__ == "__main__":
    main()
