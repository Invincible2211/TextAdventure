class Config:
    SCENE_WIDTH = 150
    SCENE_HEIGHT = 44
    ACTIONS_HEIGHT = 4
    SUB_SCENE_WIDTH = 50
    SUB_SCENE_HEIGHT = SCENE_HEIGHT + 2 + ACTIONS_HEIGHT
    PADDING = 3
    MAX_LOG_ENTRIES = SCENE_HEIGHT + 6
    MAP_ACTIONS = [
        "Aktionen:",
        "[W] Hoch, [A] Links, [S] Runter, [D] Rechts",
        "[I] Inventar, [O] Optionen",
        "Drücke 'Q' zum Beenden."
    ]
    INVENTORY_ACTIONS = [
        "Aktionen:",
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