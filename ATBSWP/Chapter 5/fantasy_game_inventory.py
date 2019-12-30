stuff = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}
dragon_loot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]


def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(v, k)
        item_total = item_total + v
    print("Total number of items: " + str(item_total))


def display_loot(loot):
    print("Loot: ")
    item_total = 0
    count = {}
    for item in loot:
        count.setdefault(item, 0)
        count[item] = count[item] + 1
    for k, v in count.items():
        print(v, k)


def add_to_inventory(inventory, added_items):
    for item in added_items:
        inventory.setdefault(item, 0)
        inventory[item] = inventory[item] + 1
    return inventory


display_inventory(stuff)

print("The dragon dropped the following items:")
display_loot(dragon_loot)

stuff = add_to_inventory(stuff, dragon_loot)
display_inventory(stuff)
