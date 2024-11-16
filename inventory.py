import log_manager


class Inventory:

    def __init__(self):
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)


    def get_items(self):
        return self.inventory