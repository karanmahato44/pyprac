# comprehension is performant than filter/map fns
items = [
    ('socks', 100),
    ('tshirt', 250),
    ('usb c dock', 4000),
    ('facewash', 50)
]

# map
prices = [item[1] for item in items]
print(prices)

# filter
expensive_items = [item for item in items if item[1] > 200]
print(expensive_items)
