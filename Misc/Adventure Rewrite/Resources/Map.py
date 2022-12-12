# crossroads = "\u256C"  # ╬
# horizontal = "\u2550"  # ═
# horizontal_down = "\u2566"  # ╦
# horizontal_up = "\u2569"  # ╩
# vertical = "\u2551"  # ║
# vertical_right = "\u2560"  # ╠
# vertical_left = "\u2563"  # ╣
# left_down = "\u2557"  # ╗
# left_up = "\u255D"  # ╝
# right_down = "\u2554"  # ╔
# right_up = "\u255A"  # ╚
# up_end = "\u2568"  # ╨
# right_end = "\u255E"  # ╞
# down_end = "\u2565"  # ╥
# left_end = "\u2561"  # ╡


def dirstochar(directions_dict):
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


def asciimap(locationgrid, playerloc=False):
    yindexes = [index for index in locationgrid]
    xindexes = [xindex for yindex in yindexes for xindex in locationgrid[yindex]]
    yrange = range(min(yindexes), max(yindexes)+1)
    xrange = range(min(xindexes), max(xindexes)+1)
    # print(yrange, xrange)
    # print(list(enumerate(yrange)))

    lines = []
    for yindex, ygrid in list(enumerate(yrange)):
        # print(yindex, ygrid)
        lines.append([])
        for xindex, xgrid in list(enumerate(xrange)):
            try:
                # print(locationgrid[ygrid][xgrid]["Doors"])
                lines[yindex].append(dirstochar(locationgrid[ygrid][xgrid]["Doors"]))
            except KeyError:
                lines[yindex].append(" ")

    for yindex, ygrid in list(enumerate(yrange)):
        for xindex, xgrid in list(enumerate(xrange))[-2::-1]:  # iterate up to index -1 in reverse (from index -2 backwards)
            #print(xindex, xgrid)
            try:
                left = locationgrid[ygrid][xgrid]
                right = locationgrid[ygrid][xgrid+1]
                #print(left, right)
                #print(left["Doors"]["East"], right["Doors"]["West"])
                if left["Doors"]["East"] and right["Doors"]["West"]:
                    lines[yindex].insert(xindex+1, "═")
                else:
                    lines[yindex].insert(xindex+1, " ")
            except KeyError:
                lines[yindex].insert(xindex+1, " ")

    for yindex, ygrid in list(enumerate(yrange))[-2::-1]:  # iterate up to index -1 in reverse (from index -2 backwards)
        lines.insert(yindex+1, [" " for _ in range(len(lines[0]))])
        for xindex, xgrid in list(enumerate(xrange)):
            xindex *= 2
            try:
                above = locationgrid[ygrid][xgrid]
                below = locationgrid[ygrid+1][xgrid]
                if above["Doors"]["South"] and below["Doors"]["North"]:
                    lines[yindex+1][xindex] = "║"
            except KeyError:
                pass

    if playerloc:
        addArrow(locationgrid, lines, "PlayerLocation", True, xrange, yrange)

    return lines


def addArrow(locationgrid, asciigrid, tag, ifValue, xrange, yrange, arrowtype="basic"):
    arrows = {"basic":    ["⭦", "⭧", "⭨", "⭩"],
              "double":   ["⇖", "⇗", "⇘", "⇙"],
              "white":    ["⬁", "⬀", "⬂", "⬃"],
              "black":    ["⬉", "⬈", "⬊", "⬋"],
              "parallel": ["⭶", "⭷", "⭸", "⭹"]}
    for yindex, ygrid in list(enumerate(yrange)):
        yindex *= 2
        # print(yindex, ygrid)
        for xindex, xgrid in list(enumerate(xrange)):
            xindex *= 2
            try:
                if locationgrid[ygrid][xgrid][tag] == ifValue:
                    for addArrow in [[arrows[arrowtype][0], 1, 1],
                                     [arrows[arrowtype][1], 1, -1],
                                     [arrows[arrowtype][2], -1, -1],
                                     [arrows[arrowtype][3], -1, 1]]:
                        try:
                            insArrowY = yindex + addArrow[1]
                            insArrowX = xindex + addArrow[2]
                            if insArrowY < 0 or insArrowX < 0:
                                pass
                            else:
                                if not asciigrid[insArrowY][insArrowX] in [arrow for arrowset in list(arrows.values()) for arrow in arrowset]:
                                    asciigrid[insArrowY][insArrowX] = addArrow[0]
                                    break
                        except IndexError:
                            pass
            except KeyError:
                pass


def getmap(grid, playerloc=True):
    mapped = asciimap(grid, playerloc)
    for line in mapped:
        print("".join(line))
    #print(mapped)

