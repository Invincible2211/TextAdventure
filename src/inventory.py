from observable import Observable


class Inventory(Observable):

    def __init__(self):
        super().__init__()
        self.inventory = []
        self.cursor = 0

    def add_item(self, item):
        self.inventory.append(item)
        self.notify_observers(self.get_items(), self.cursor)


    def get_items(self):
        return self.inventory

    def remove_item(self, index):
        self.inventory.pop(index)
        self.notify_observers(self.get_items(), self.cursor)

    def get_selected_item(self):
        return self.inventory[self.cursor]

    def cursor_up(self):
        self.cursor = max(0, self.cursor - 1)
        self.notify_observers(self.get_items(), self.cursor)

    def cursor_down(self):
        self.cursor = min(len(self.inventory) - 1, self.cursor + 1)
        self.notify_observers(self.get_items(), self.cursor)