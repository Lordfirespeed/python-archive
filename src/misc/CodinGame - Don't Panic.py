fln, width, rn, exf, exp, nbtc, nbae, nbe = [int(i) for i in input().split()]
elevators = dict([[int(i) for i in input().split()] for n in range(nbe)])
elevators[exf] = exp

while True:
    clone_floor, clone_pos, direction = input().split()
    clone_floor = int(clone_floor)
    clone_pos = int(clone_pos)

    if [clone_floor, clone_pos, direction] == [-1, -1, "NONE"]:
        cmd = "WAIT"
    else:

        elev_direction = "LEFT" if clone_pos > elevators[clone_floor] else "RIGHT"

        above_elevator = (clone_pos == elevators[clone_floor - 1] if clone_floor > 0 else True) if len(elevators) > 0 else True

        if clone_pos == 0 or clone_pos == width - 1:
            cmd = "BLOCK"
        elif clone_pos == elevators[clone_floor]:
            cmd = "WAIT"
        elif (not above_elevator) and elev_direction != direction:
            cmd = "BLOCK"
        else:
            cmd = "WAIT"

    print(cmd)