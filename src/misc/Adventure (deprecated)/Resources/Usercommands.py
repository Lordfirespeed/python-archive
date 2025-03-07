def go(direction, valid_directions):
    # command = command[:-1]
    # command += ', valid_ways)'
    
    coord_map = {"North":"y += 1", "East":"x += 1", "South":"y -= 1", "West":"x -= 1"}
    if not direction.title() in valid_directions:
        return ["print('Invalid direction.')"]
    else:
        commands = []
        commands.append(coord_map[direction.title()])
        commands.append("last_direction = '" + direction.title() + "'")
        commands.append("print('Went " + direction.title() + ".')")
        commands.append("print()")
        commands.append("moved = True")
        return commands
    
def map():
    commands = []
    commands.append("printable_map = mapfuncs.ascii_map(list(NE_map_array), list(SE_map_array), list(SW_map_array), list(NW_map_array))")
    commands.append("for line in printable_map:\n    print(line)")
    return commands
