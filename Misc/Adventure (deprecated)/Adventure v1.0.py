import random

def validinput(message, acceptable):
    while True:
        print(message)
        userinput = input("> ")
        if not userinput.title() in acceptable:
            print("Invalid input.")
        else:
            return userinput.title()

def genroom(array, x, y, entry):
    while len(array) < (x+1):
        array.append([])
              
    while len(array[x]) < (y+1):
        array[x].append([])

    open_ways = [random.choice(chance_open) for door in range(4)]
    open_ways_dict = {}
    for index, way in enumerate(open_ways):
        open_ways_dict[directions[index]] = way
    open_ways_dict[opposites[entry]] = True
        
    array[x][y] = [False, open_ways_dict]
                
x = 0
y = 0
directions = ["North", "East", "South", "West"]
coord_map = {"North":"y += 1", "East":"x += 1", "South":"y -= 1", "West":"x -= 1"}

opposites = {"North":"South", "East":"West", "South":"North", "West":"East"}
chance_open = [True, False]

NE_map_array = [[[True, {"North":True, "East":True, "South":True, "West":True}]]]
NW_map_array = [[]]
SE_map_array = [[]]
SW_map_array = [[]]

print("You have entered the dungeon. \nYou enter from above, via a stepladder in the centre of a circular room.\nIn each direction a dark hallway extends from the room.")


# mainloop
while True:
    # Entering a room

    # Select correct map array
    if x >= 0 and y >= 0:
        use_x = x
        use_y = y
        map_array = NE_map_array
    elif x >= 0 and y < 0:
        use_x = x
        use_y = -1 * y
        map_array = SE_map_array
    elif x < 0 and y < 0:
        use_x = -1 * x
        use_y = -1 * y
        map_array = SW_map_array
    elif x < 0 and y >= 0:
        use_x = -1 * x
        use_y = y
        map_array = NW_map_array
    else:
        pass

    failed = True
    while failed:
        try:
            thing = map_array[use_x][use_y][0]
            break
        except IndexError:
            # Generate a new room at the current coords
            genroom(map_array, use_x, use_y, last_direction)
            
    if map_array[use_x][use_y][0]:
        # Room explored already / Room is start room
        pass
    else:
        # Room not explored. Do an encounter. (pass, for now)
        map_array[use_x][use_y][0] = True
        pass

    ways = map_array[use_x][use_y][1]

    all_open = True
    for direction in ways:
        if ways[direction]:
            pass
        else:
            all_open = False

    valid_ways = [direction for direction in ways if ways[direction]]
    if all_open:
        print("You are at a crossroads. You can go in any direction.")
    else:
        valid_ways[-1] = "or " + valid_ways[-1]
        print("You are at a crossroads. You may go " + ", ".join(valid_ways) + ".")
        valid_ways[-1] = valid_ways[-1].replace("or ", "")

    direction_input = validinput("Which way will you go?", directions)
    last_direction = direction_input
    exec(coord_map[direction_input])
    print()
