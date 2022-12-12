# map list
Rooms = [
    [1, {"North":2, "East":3,"West":4}],
    [2, {"South":1}],
    [3, {"West":1}],
    [4, {"East":1}]
    ]

# variable initialisation
currentroom = 1
directions = ["North", "East", "South", "West"]

while True:
    print("You are in " + str(currentroom) + ".")
    valid_directions = {}
    for place in Rooms:
        if place[0] == currentroom:
            for direction in place[1]:
                print("To the " + direction + ": " + str(place[1][direction]) + ".")
                valid_directions[direction] = place[1][direction]
            break
        
    print("Which way would you like to go?")
    direction_input_valid = False
    while not direction_input_valid:
        direction_input = input("> ").title()
        if direction_input in directions:
            if direction_input in valid_directions:
                direction_input_valid = True
                print("You went " + direction_input + ", into " + str(valid_directions[direction_input]) + ".")
                currentroom = valid_directions[direction_input]
            else:
                print("You cannot go that way. A wall blocks your path.")
                direction_input_valid = False
        else:
            direction_input_valid = False
            print("Invalid direction.")
    print()

        
        
