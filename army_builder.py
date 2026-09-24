valid_units = {
    "farseer": 80,
    "autarch": 75,
    "guardian defenders": 100,
    "storm guardians": 100,
    "sire avengers": 75,
    "howling banshees": 95,
    "dark reapers": 95,
    "swooping hawks": 95,
    "fire dragons": 120,
    "warp spiders": 105,
    "shining spears": 100,
    "wraithguard": 170,
    "wraithlord": 140,
    "war walker": 95,
    "wave serpent": 120,
    "falcon": 130
}

print("Welcome to the Eldar Army Builder for Warhammer: 40,000.\nHere are the current units you can add and their points values:\n")
for valid_unit, value in valid_units.items():
    print(f"{valid_unit.title()}: {value}")
while True:
    army_list = []
    total_points = 0
    unit = input("\nAdd a unit to your army list: ").lower()
    if unit in valid_units:
        army_list.append(unit)