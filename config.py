class Config:
    SCENE_WIDTH = 150
    SCENE_HEIGHT = 44
    ACTIONS_HEIGHT = 4
    SUB_SCENE_WIDTH = 50
    SUB_SCENE_HEIGHT = SCENE_HEIGHT + 2 + ACTIONS_HEIGHT
    PADDING = 3
    ACTION_DELAY = 0.2
    MAX_LOG_ENTRIES = SCENE_HEIGHT + 6
    MAP_ACTIONS = [
        "Steuerung:",
        "[W] Hoch, [A] Links, [S] Runter, [D] Rechts",
        "[E] Interagieren, [I] Inventar, [T] Team, [O] Optionen",
        "\033[31mDrücke 'Q' zum Beenden.\033[0m"
    ]
    INVENTORY_ACTIONS = [
        "",
        "Drücke [B], um zurückzukehren.",
        " ",
        " "
    ]
    TITLE = [
        "  ___              _  _                          ",
        " / _ \\            (_)(_)                         ",
        "/ /_\\ \\ ___   ___  _  _  _ __ ___    ___   _ __  ",
        "|  _  |/ __| / __|| || || '_ ` _ \\  / _ \\ | '_ \\ ",
        "| | | |\\__ \\| (__ | || || | | | | || (_) || | | |",
        "\\_| |_/|___/ \\___||_||_||_| |_| |_| \\___/ |_| |_|"
    ]