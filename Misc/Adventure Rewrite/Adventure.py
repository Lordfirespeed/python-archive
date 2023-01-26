from Resources.Map import getmap
import Resources.Misc as misc

oppositedirections = {"North": "South", "East": "West", "South": "North", "West": "East"}
directiontocoords = {"North": [-1, 0], "East": [0, 1], "South": [1, 0], "West": [0, -1]}


def directionsmessage(ways):
    boolways = [ways[direction] for direction in ["North", "East", "South", "West"]]
    textways = [direction for direction in ["North", "East", "South", "West"] if ways[direction]]
    if all(boolways):
        print("You find yourself at a crossroads. You can go in any direction.")
    elif boolways.count(True) == 1:
        print("You reach a dead end. You may go back, " + "".join(textways) + ".")
    else:
        if boolways.count(True) == 2:
            if textways[0] == oppositedirections[textways[1]]:
                startmessage = "A darkened corridor extends ahead of you. "
            else:
                startmessage = "You come across a turning. "
        else:
            startmessage = "You come to a fork in the path. "
        textways[-1] = "or " + textways[-1]
        print(startmessage + "You may go " + ", ".join(textways) + ".")


def genroom(y, x):
    global grid
    room = {"Doors": dict([[direction, misc.boolprob(6, 10)] for direction in ["North", "East", "South", "West"]]),
            "PlayerLocation": False}
    adjacent = [
        ["North", (y + 1), x],  # Room below
        ["West", y, (x + 1)],  # Room to the right
        ["South", (y - 1), x],  # Room above
        ["East", y, (x - 1)]  # Room to the left
    ]

    # Check the four adjacent rooms
    for place in adjacent:
        try:
            room["Doors"][oppositedirections[place[0]]] = grid[place[1]][place[2]]["Doors"][place[0]]
        except KeyError:
            pass

    grid[y][x] = dict(room)


def move(direction):
    global currentlocation
    global grid
    direction = direction.title()
    y = currentlocation[0]
    x = currentlocation[1]
    if not grid[y][x]["Doors"][direction]:
        print("A wall stands in your path, defiant by nature.")
        return None
    grid[y][x]["PlayerLocation"] = False
    changecoords = directiontocoords[direction]
    y, x = y + changecoords[0], x + changecoords[1]
    if y not in grid:
        grid[y] = {}
    if x not in grid[y]:
        genroom(y, x)
    directionsmessage(grid[y][x]["Doors"])
    currentlocation = [int(y), int(x)]
    grid[y][x]["PlayerLocation"] = True


grid = {0: {0: {"Doors": {"North": True, "East": True, "South": True, "West": True}, "PlayerLocation": True}}}
currentlocation = [0, 0]

print("""You have entered the dungeon. 
You enter from above, via a stepladder in the centre of a circular room.
In each direction a dark hallway extends from the room.""")
directionsmessage(grid[0][0]["Doors"])
