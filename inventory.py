from observable import Observable


class Inventory(Observable):

    def __init__(self):
        super().__init__()
        self.inventory = []
        self.cursor = 0

    def add_item(self, item):
        self.inventory.append(item)
        self.notify_observers(self.get_items())


    def get_items(self):
        return self.inventory