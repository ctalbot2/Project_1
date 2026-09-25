
valid_units = {
    "farseer": 80,
    "autarch": 75,
    "guardian defenders": 100,
    "storm guardians": 100,
    "dire avengers": 75,
    "howling banshees": 95,
    "dark reapers": 95,
    "swooping hawks": 95,
    "fire dragons": 120,
    "warp spiders": 105,
    "shining spears": 100,
    "wraithguard": 170,
    "wraithlord": 140,
    "wraithknight": 400,
    "war walker": 95,
    "wave serpent": 120,
    "falcon": 130
}
battleline_units = [
    "guardian defenders",
    "storm guardians"
]
"""
this is the set of units you're allowed to add to your army.  each unit has a points cost defined in the game's rules
"""

army_list = []
total_points = 0
"""
army_list and total_points is what the user is trying to balance.  for a game of this type, the army's total points can't be >2,000
"""

print("Welcome to the Eldar Army Builder for Warhammer: 40,000.\nHere are the current units you can add and their points values:\n")
for valid_unit, value in valid_units.items():
    print(f"{valid_unit.title()}: {value}")
    """
    this is the opening message that lets the user know the valid units
    """

while True:
    """
    the program's while loop
    """
    unit = input("\nAdd a unit to your army list: ").lower()
    if unit in valid_units:
        if unit not in battleline_units and army_list.count(unit) >= 3:
            print(f"\nYou cannot add more than three {unit.title()} units.")
        elif unit in battleline_units and army_list.count(unit) >= 6:
            print(f"You cannot add more than six {unit.title()} units")
        elif total_points + valid_units[unit] <= 2000:
            """
            checks total army points cost before adding to the army
            """
            army_list.append(unit)
            total_points = sum(valid_units[unit] for unit in army_list)
            print(f"\nAdded unit: {unit.title()}")
        else:
            print("\nLooks like your army would go over 2,000 points. You cannot add that unit.")
    else:
        print("\nThat is not a valid unit.")
    
    print(army_list)
    print(total_points)
    """
    the bottom code helps with debugging
    """