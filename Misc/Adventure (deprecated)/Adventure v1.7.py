import random
import Map

def select_map_array(x, y):
    global NE_map_array
    global SE_map_array
    global SW_map_array
    global NW_map_ma
    return_list = []
    if x >= 0 and y >= 0:
        return_list.append(x)
        return_list.append(y)
        return_list.append(NE_map_array)
    elif x >= 0 and y < 0:
        return_list.append(x)
        return_list.append((-1 * y) - 1)
        return_list.append(SE_map_array)
    elif x < 0 and y < 0:
        return_list.append((-1 * x) - 1)
        return_list.append((-1 * y) - 1)
        return_list.append(SW_map_array)
    elif x < 0 and y >= 0:
        return_list.append((-1 * x) - 1)
        return_list.append(y)
        return_list.append(NW_map_array)
    return return_list

def validinput(message, acceptable):
    while True:
        print(message)
        userinput = input("> ")
        if not userinput.title() in acceptable:
            print("Invalid input.")
        else:
            return userinput.title()

def genroom(x, y, entry):
    gen_x, gen_y, gen_array = select_map_array(x, y)
    
    while len(gen_array) < (gen_x+1):
        gen_array.append([])
              
    while len(gen_array[gen_x]) < (gen_y+1):
        gen_array[gen_x].append([])

    # Generate randomly open / closed doors
    open_ways = [random.choice(chance_open) for door in range(4)]
    open_ways_dict = {}
    for index, way in enumerate(open_ways):
        open_ways_dict[directions[index]] = way

    # Set the entry door to open
    open_ways_dict[opposites[entry]] = True

    # Get the coordinates of the four adjacent rooms
    adjacent = [
        ["South", (x), (y+1)],
        ["West", (x+1), (y)],
        ["North", (x), (y-1)],
        ["East", (x-1), (y)]
    ]
    
    # Check the four adjacent rooms
    for room in adjacent:
        check_x, check_y, check_array = select_map_array(room[1], room[2])
        try:
            open_ways_dict[opposites[room[0]]] = check_array[check_x][check_y][1][room[0]]
        except IndexError:
            pass
      
    gen_array[gen_x][gen_y] = [False, open_ways_dict]
                
x = 0
y = 0
directions = ["North", "East", "South", "West"]
coord_map = {"North":"y += 1", "East":"x += 1", "South":"y -= 1", "West":"x -= 1"}

valid_commands = ["Go", "Map"]

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
    use_x, use_y, map_array = select_map_array(x, y)

    failed = True
    while failed:
        try:
            thing = map_array[use_x][use_y][0]
            break
        except IndexError:
            # Generate a new room at the current coords
            genroom(x, y, last_direction)
            
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
    elif len(valid_ways) == 1:
        print("You have reached a dead end. You may go back, " +
            "".join(valid_ways) + ".")
    else:
        valid_ways[-1] = "or " + valid_ways[-1]
        print("You are at a crossroads. You may go " + ", ".join(valid_ways) + ".")
        valid_ways[-1] = valid_ways[-1].replace("or ", "")

    try:
        direction_input = validinput("Which way will you go?", valid_ways)
    except KeyboardInterrupt:
        break
    last_direction = direction_input
    exec(coord_map[direction_input])
    print()

Map.ascii_map(NE_map_array, SE_map_array, SW_map_array, NW_map_array)

