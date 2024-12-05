# text_utils.py

import re


def count_ansi_length(text):
    """
    Berechnet die Länge der ANSI-Sequenzen in einem Text.
    """
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return sum(len(seq) for seq in ansi_escape.findall(text))


def frame_text(text, width, height, title=""):
    """
    Rendert den Text innerhalb eines Rahmens mit angegebener Breite und Höhe.
    Gibt ein String-Tupel zurück, das die gerenderte Darstellung des Rahmens und des Textes enthält.
    """
    title_line = f"╔{title.center(width + count_ansi_length(title), '═')}╗" if title else f"╔{'═' * width}╗"
    lines = [title_line]

    # Text in die Zeilen einfügen
    for i in range(height):
        line_content = text.get_line(i) if text else ""
        line_content = line_content.ljust(width + count_ansi_length(line_content))
        lines.append(f"║{line_content}║")

    # Untere Rahmenlinie
    lines.append(f"╚{'═' * width}╝")

    return tuple(lines)
