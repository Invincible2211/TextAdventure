import os
import sys
import time
import keyboard

from config import Config
from inventory import Inventory
from ui.action_container import ActionContainer
from ui.scenes.fight_scene import FightScene
from ui.sub_scene.inventory_scene import InventoryScene
from log_manager import LogManager
from ui.sub_scene.log_scene import LogScene
from map_manager import MapManager
from ui.scenes.map_scene import MapScene
from player import Player
from ui.ui_manager import UIManager, clear_screen

# Für Unix (Linux/macOS)
if os.name == 'posix':
    import termios

    def reset_input():
        """Leert den Eingabepuffer auf Unix-Systemen (Linux/macOS)."""
        termios.tcflush(sys.stdin, termios.TCIFLUSH)

# Für Windows
elif os.name == 'nt':
    import msvcrt

    def reset_input():
        """Leert den Eingabepuffer auf Windows-Systemen."""
        while msvcrt.kbhit():
            msvcrt.getch()  # Liest ein Zeichen und verwirft es


def get_user_input(valid_actions):
    while True:
        for action in valid_actions:
            if keyboard.is_pressed(action.lower()) or keyboard.is_pressed(action.upper()):
                reset_input()
                return action


class Game:
    def __init__(self):
        # Initialisierung

        self.ui_manager = UIManager()

        self.map_scene = MapScene(self.ui_manager)
        self.map_manager = MapManager(" ")
        self.map_manager.load_map_from_file("map.txt")

        self.map_manager.register_observer(self.map_scene)

        self.player = Player(Config.SCENE_WIDTH // 2, Config.SCENE_HEIGHT // 2, "Fynn")
        self.map_manager.update_tile(self.player.x, self.player.y, self.player.symbol)

        log_manager = LogManager(Config.MAX_LOG_ENTRIES)
        LogManager.set_instance(log_manager)

        self.log_scene = LogScene()
        log_manager.register_observer(self.log_scene)

        self.player_inventory = Inventory()
        self.inventory_scene = InventoryScene()

        self.player_inventory.register_observer(self.inventory_scene)

        self.fight_scene = FightScene()

        LogManager.add_entry("Spiel gestartet.")

        self.actions = ActionContainer()

        self.scene = None
        self.sub_scene = None

        # Initialzustand
        self.state = ""
        self.switch_state("MainGame")
        self.running = True

    def main(self):
        # Cursor ausblenden
        sys.stdout.write("\033[?25l")

        while self.running:
            self.ui_manager.render(self.scene, self.sub_scene, self.actions)
            if self.state == "MainMenu":
                self.main_menu()
            elif self.state == "CreateGame":
                self.create_game()
            elif self.state == "ResumeGame":
                self.resume_game()
            elif self.state == "StartDialog":
                self.start_dialog()
            elif self.state == "MainGame":
                self.main_game()
            elif self.state == "Inventory":
                self.inventory()
            elif self.state == "Options":
                self.options()
            elif self.state == "Fight":
                self.fight()
            elif self.state == "Exit":
                self.exit_game()
            start_time = time.time()
            while time.time() - start_time < Config.ACTION_DELAY:
                time.sleep(0.01)  # Reduziert CPU-Last

        # Cursor wieder einblenden
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()
        clear_screen()

    def main_menu(self):
        LogManager.add_entry("Hauptmenü geöffnet.")
        # Menülogik (Beispielhaft)
        while True:
            action = get_user_input(["N", "L", "Q"])  # Neues Spiel, Laden, Beenden
            if action == "N":
                self.state = "CreateGame"
                break
            elif action == "L":
                self.state = "ResumeGame"
                break
            elif action == "Q":
                self.state = "Exit"
                break

    def create_game(self):
        LogManager.add_entry("Neues Spiel erstellt.")
        self.state = "StartDialog"

    def resume_game(self):
        LogManager.add_entry("Spiel fortgesetzt.")
        self.state = "MainGame"

    def start_dialog(self):
        LogManager.add_entry("Dialog gestartet.")
        # Dialoglogik (Platzhalter)
        self.state = "MainGame"

    def main_game(self):
        action = get_user_input(["Q", "W", "A", "S", "D", "E", "I", "O"])
        if action == "Q":
            self.switch_state("Exit")
        elif action in ["W", "A", "S", "D"]:
            self.handle_player_movement(action)
        elif action == "E":
            LogManager.add_entry(f"Interaktionsversuch von {self.player.name}: {self.player.check_tile_in_front(self.map_manager)}")
        elif action == "I":
            self.switch_state("Inventory")
        elif action == "O":
            self.switch_state("Options")

    def inventory(self):
        action = get_user_input(["E", "Up", "Down", "B"])
        if action == "E":
            LogManager.add_entry(f"Item ausgewählt: {self.player_inventory.get_selected_item()}")
        if action == "Up":
            self.player_inventory.cursor_up()
        if action == "Down":
            self.player_inventory.cursor_down()
        if action == "B":
            self.switch_state("MainGame")

    def options(self):
        LogManager.add_entry("Optionen geöffnet.")
        self.state = "MainGame"

    def fight(self):
        LogManager.add_entry("Kampf begonnen")
        self.state = "MainGame"

    def exit_game(self):
        LogManager.add_entry("Spiel beendet.")
        self.running = False

    def handle_player_movement(self, action):
        if not self.player.move(action, self.map_manager):
            LogManager.add_entry(f"Bewegung nach {action} blockiert.")

    def switch_state(self, state):
        self.state = state
        if self.state == "MainMenu":
            pass
        elif self.state == "CreateGame":
            pass
        elif self.state == "ResumeGame":
            pass
        elif self.state == "StartDialog":
            pass
        elif self.state == "MainGame":
            self.scene = self.map_scene
            self.sub_scene = self.log_scene
            self.actions.set_actions(Config.MAP_ACTIONS)
        elif self.state == "Inventory":
            LogManager.add_entry("Inventar geöffnet.")
            self.player_inventory.add_item("Schwert")
            self.player_inventory.add_item("Schild")
            self.sub_scene = self.inventory_scene
            self.actions.set_actions(Config.INVENTORY_ACTIONS)
        elif self.state == "Options":
            pass
        elif self.state == "Exit":
            pass

# Hauptprogramm
if __name__ == "__main__":
    game = Game()
    game.main()