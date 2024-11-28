class Scene:
    def __init__(self, width, height, title="", fill_char=" "):
        self.width = width
        self.height = height
        self.title = title
        self.fill_char = fill_char
        self.content = []
        self.dirty = False

    def get_line(self, index):
        """
        Gibt die Zeile an der gegebenen Indexposition zurück, oder eine leere Zeile, wenn der Index ungültig ist.
        """
        if 0 <= index < len(self.content):
            return ''.join(self.content[index])
        return self.fill_char * self.width

    def get_title(self):
        return self.title
