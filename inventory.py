class Inventory:
    __capacity = 0
    items = []

    def __init__(self, capacity):
        self.__capacity = capacity

    def add_item(self, item):
        if len(self.items) < self.__capacity:
            self.items.append(item)

        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        result = ""
        # result += Items: {items}.\nCapacity left: {left_capacity}
        result += "Items: "
        result += ", ".join(self.items)
        result += f".\nCapacity left: {self.__capacity - len(self.items)}"
        return result


inventory = Inventory(1)
inventory.add_item("potion")
print(inventory.add_item("sword"))

print(inventory.get_capacity())
print(inventory)
