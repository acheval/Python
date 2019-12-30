stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(v, k)
        item_total = item_total + v
    print("Total number of items:" + str(item_total))

def add_to_inventory(inventory, added_items):
    count = {}
    for item in added_items:
        count.setdefault(item, 0)
        count[inventory] = count[inventory] + 1
    return inventory 

display_inventory(stuff)

stuff = add_to_inventory(stuff, dragon_loot)
display_inventory(stuff)
