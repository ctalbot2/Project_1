valid_units = {
    "Farseer": 80,
    "Autarch": 75,
    "Guardian Defenders": 100,
    "Storm Guardians": 100,
    "Dire Avengers": 75,
    "Howling Banshees": 95,
    "Dark Reapers": 95,
    "Swooping Hawks": 95,
    "Fire Dragons": 120,
    "Warp Spiders": 105,
    "Shining Spears": 100,
    "Wraithguard": 170,
    "Wraithlord": 140,
    "War Walker": 95,
    "Wave Serpent": 120,
    "Falcon": 130
}

print("Welcome to the Eldar Army Builder for Warhammer: 40,000.\nHere are the current units you can add and their points values:\n")
for valid_unit, value in valid_units.items():
 print(f"{valid_unit}: {value}")