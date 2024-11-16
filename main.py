import sys
import time

import keyboard

from config import Config
from inventory import Inventory
from inventory_scene import InventoryScene
from log_manager import LogManager
from log_scene import LogScene
from map_manager import MapManager
from map_scene import MapScene
from player import Player
from ui_manager import UIManager, clear_screen, set_scene_dirty, set_actions_dirty, set_sub_scene_dirty


def main():
    # Initialisierung
    map_manager = MapManager(" ")
    map_manager.load_map_from_file("map.txt")

    player = Player(Config.SCENE_WIDTH // 2, Config.SCENE_HEIGHT // 2)
    map_manager.update_tile(player.x, player.y, player.symbol)

    map_scene = MapScene(map_manager)
    map_scene.refresh()

    log_manager = LogManager(Config.MAX_LOG_ENTRIES)
    log_manager.add_entry("Spiel gestartet.")

    log_scene = LogScene(log_manager)
    log_manager.add_scene(log_scene)

    ui_manager = UIManager()
    ui_manager.render(map_scene, log_scene, Config.MAP_ACTIONS)

    # Cursor ausblenden
    sys.stdout.write("\033[?25l")

    while True:
        action_performed = False  # Flag, um festzustellen, ob eine Aktion ausgeführt wurde
        action = None

        # Warte auf Tastendruck
        if keyboard.is_pressed("q"):
            action = "Q"
        elif keyboard.is_pressed("w"):
            action = "W"
        elif keyboard.is_pressed("a"):
            action = "A"
        elif keyboard.is_pressed("s"):
            action = "S"
        elif keyboard.is_pressed("d"):
            action = "D"
        elif keyboard.is_pressed("i"):
            action = "I"
        elif keyboard.is_pressed("o"):
            action = "O"

        if action:
            action_performed = True  # Eine Aktion wurde ausgeführt

            # Verarbeite die Aktion
            if action == "Q":
                log_manager.add_entry("Spiel beendet.")
                clear_screen()
                # Cursor wieder einblenden
                sys.stdout.write("\033[?25h")
                sys.stdout.flush()
                break
            elif action in ["W", "A", "S", "D"]:
                if player.move(action, map_manager):
                    map_scene.refresh()
                    set_scene_dirty()
                    set_sub_scene_dirty()
                    log_manager.add_entry(f"Spieler bewegte sich nach {action}.")
                else:
                    log_manager.add_entry(f"Bewegung nach {action} blockiert.")
            elif action == "I":
                log_manager.add_entry("Inventar geöffnet.")
                set_sub_scene_dirty()
                set_actions_dirty()
                inventory = Inventory()
                inventory.add_item("Schwert")
                inventory.add_item("Schild")
                inventory_scene = InventoryScene(inventory)
                inventory_scene.refresh()

                while True:
                    ui_manager.render(map_scene, inventory_scene, Config.INVENTORY_ACTIONS)
                    dialog_action = None
                    if keyboard.is_pressed("b"):
                        dialog_action = "B"

                    if dialog_action == "B":
                        log_manager.add_entry("Inventar geschlossen.")
                        set_actions_dirty()
                        set_sub_scene_dirty()
                        break
            elif action == "O":
                log_manager.add_entry("Optionen geöffnet.")
            else:
                log_manager.add_entry("Ungültige Eingabe.")

            # Blockiere für den Delay
            start_time = time.time()
            while time.time() - start_time < Config.ACTION_DELAY:
                time.sleep(0.05)  # Reduziert CPU-Last

        # Render nur ausführen, wenn eine Aktion durchgeführt wurde
        if action_performed:
            ui_manager.render(map_scene, log_scene, Config.MAP_ACTIONS)

if __name__ == "__main__":
    main()
