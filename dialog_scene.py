from Scene import Scene


class DialogScene(Scene):
    def __init__(self, width, height, dialog_lines):
        super().__init__(width, height)
        self.load_dialog(dialog_lines)

    def load_dialog(self, dialog_lines):
        """
        Lädt Dialogzeilen und passt sie an die Szenen-Größe an.
        """
        adjusted_content = []
        for line in dialog_lines:
            adjusted_content.append(list(line.ljust(self.width, self.fill_char)))
        while len(adjusted_content) < self.height:
            adjusted_content.append([self.fill_char] * self.width)
        self.content = adjusted_content[:self.height]
