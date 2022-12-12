crossroads = "\u256C"  # ╬
horizontal = "\u2550"  # ═
horizontal_down = "\u2566"  # ╦
horizontal_up = "\u2569"  # ╩
vertical = "\u2551"  # ║
vertical_right = "\u2560"  # ╠
vertical_left = "\u2563"  # ╣
left_down = "\u2557"  # ╗
left_up = "\u255D"  # ╝
right_down = "\u2554"  # ╔
right_up = "\u255A"  # ╚
up_end = "\u2568"  # ╨
right_end = "\u255E"  # ╞
down_end = "\u2565"  # ╥
left_end = "\u2561"  # ╡


def array(list_thing):
    if not list_thing:
        return []
    elif list_thing == [[]]:
        return [[]]
    else:
        newarray = []
        for x in list_thing:
            newarrayline = []
            for xy in x:
                newarrayline.append(xy)
            newarray.append(newarrayline)
        return newarray
                

def flip_arrays(NE, SE, SW, NW):
    # Reverse X and Y of NW map
    NW.reverse()
    for x_column in NW:
        x_column.reverse()

    # Reverse Y of NE map
    for x_column in NE:
        x_column.reverse()

    # Reverse X of SW map
    SW.reverse()

    return [NE, SE, SW, NW]


def map_grid(NE_map_array_1, SE_map_array_2, SW_map_array_3, NW_map_array_4):
    NE_print_array = array(NE_map_array_1)
    SE_print_array = array(SE_map_array_2)
    SW_print_array = array(SW_map_array_3)
    NW_print_array = array(NW_map_array_4)

    NE_print_array, SE_print_array, SW_print_array, NW_print_array = flip_arrays(NE_print_array, SE_print_array, SW_print_array, NW_print_array)

    # Normalise X length of SW and NW
    W_length = max([len(SW_print_array), len(NW_print_array)])
    while len(SW_print_array) < W_length:
        SW_print_array.insert(0, [])
    while len(NW_print_array) < W_length:
        NW_print_array.insert(0, [])

    # Normalise X length of SE and NE
    E_length = max([len(SE_print_array), len(NE_print_array)])
    while len(SE_print_array) < E_length:
        SE_print_array.append([])
    while len(NE_print_array) < E_length:
        NE_print_array.append([])

    # Normalise Y length of NW and NE
    NW_height = max([len(x_column) for x_column in NW_print_array])
    NE_height = max([len(x_column) for x_column in NE_print_array])
    N_height = max([NW_height, NE_height])
    for x_column in NW_print_array:
        while len(x_column) < N_height:
            x_column.insert(0, [])
    for x_column in NE_print_array:
        while len(x_column) < N_height:
            x_column.insert(0, [])

    # Normalise Y length of SW and SE
    SW_height = max([len(x_column) for x_column in SW_print_array])
    SE_height = max([len(x_column) for x_column in SE_print_array])
    S_height = max([SW_height, SE_height])
    for x_column in SW_print_array:
        while len(x_column) < S_height:
            x_column.append([])
    for x_column in SE_print_array:
        while len(x_column) < S_height:
            x_column.append([])

    # Stitch the north and south regions together, separately
    N_region = list(NW_print_array) + list(NE_print_array)
    S_region = list(SW_print_array) + list(SE_print_array)
    
    # Stitch the N_region and S_region together by appending the x_columns
    full_region = list(N_region)
    for index, x_column in enumerate(full_region, 0):
        full_region[index] += S_region[index]

    NE_print_array = []
    SE_print_array = []
    SW_print_array = []
    NW_print_array = []

    print("\n".join([str(i) for i in full_region]))

    return full_region


def dirs_to_char(directions_dict):
    crossroads = "\u256C"  # ╬
    horizontal = "\u2550"  # ═
    horizontal_down = "\u2566"  # ╦
    horizontal_up = "\u2569"  # ╩
    vertical = "\u2551"  # ║
    vertical_right = "\u2560"  # ╠
    vertical_left = "\u2563"  # ╣
    left_down = "\u2557"  # ╗
    left_up = "\u255D"  # ╝
    right_down = "\u2554"  # ╔
    right_up = "\u255A"  # ╚
    up_end = "\u2568"  # ╨
    right_end = "\u255E"  # ╞
    down_end = "\u2565"  # ╥
    left_end = "\u2561"  # ╡
    
    up = directions_dict["North"]
    right = directions_dict["East"]
    down = directions_dict["South"]
    left = directions_dict["West"]

    if up and right and down and left:
        return crossroads
    
    elif left and right and not down and not up:
        return horizontal
    elif left and right and down and not up:
        return horizontal_down
    elif left and right and up and not down:
        return horizontal_up

    elif up and down and not left and not right:
        return vertical
    elif up and down and right and not left:
        return vertical_right
    elif up and down and left and not right:
        return vertical_left

    elif left and down and not up and not right:
        return left_down
    elif left and up and not down and not right:
        return left_up
    elif right and down and not up and not left:
        return right_down
    elif right and up and not down and not left:
        return right_up

    elif up and not right and not down and not left:
        return up_end
    elif not up and right and not down and not left:
        return right_end
    elif not up and not right and down and not left:
        return down_end
    elif not up and not right and not down and left:
        return left_end
    
    else:
        return "BAD"


def ascii_map(NE_array, SE_array, SW_array, NW_array):
    array_1 = array(NE_array)
    array_2 = array(SE_array)
    array_3 = array(SW_array)
    array_4 = array(NW_array)
    region = map_grid(array_1, array_2, array_3, array_4)
    maxwidth = max([len(x_column) for x_column in region])
    ascii_list = []
    for y in range(maxwidth):
        line_list = []
        for x in range(len(region)):
            try:
                if region[x][y][0]:
                    line_list.append(dirs_to_char(region[x][y][1]))
            except IndexError:
                line_list.append(" ")
        ascii_list.append("".join(line_list))
    return ascii_list
