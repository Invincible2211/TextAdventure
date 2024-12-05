# text_utils.py

def center_text_in_bounds(text, width, height):
    """
    Zentriert den gegebenen Text innerhalb der angegebenen Breite und Höhe.
    Gibt die zentrierten Textzeilen als Tupel zurück, ohne einen Rahmen zu setzen.
    """
    # Berechnung der maximalen Zeilenanzahl, die in den angegebenen Bereich passt
    lines = text.split('\n')
    centered_lines = []

    # Für jede Zeile den Text zentrieren und in die zentrierten Zeilen aufnehmen
    for line in lines:
        centered_line = line.center(width)
        centered_lines.append(centered_line[:width])  # Stellt sicher, dass die Zeile nicht breiter als die Grenzen wird

    # Wenn die Anzahl der Zeilen kleiner als die Höhe ist, Leerzeilen hinzufügen
    while len(centered_lines) < height:
        centered_lines.append(" " * width)

    return tuple(centered_lines)
