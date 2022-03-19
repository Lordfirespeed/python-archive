def rotate(rope):
    rope.insert(0, rope.pop())


def check_solution(top, bottom, required):
    for position, value in required.items():
        if top[position] + bottom[position] != value:
            return False
    return True


def solve(top, bottom, required):
    top = top.copy()
    bottom = bottom.copy()
    top_rotations = 0
    bottom_rotations = 0

    while not check_solution(top, bottom, required):
        rotate(bottom)
        if bottom_rotations >= 6:
            bottom_rotations = 0
            rotate(top)
            top_rotations += 1
            if top_rotations >= 6:
                return None
        else:
            bottom_rotations += 1

    if bottom_rotations >= 5:
        bottom_rotations = 0
    else:
        bottom_rotations += 1

    return top_rotations, bottom_rotations


def main():
    top = [1, 2, 1, 2, 1, 3]
    bottom = [2, 1, 3, 2, 1, 1]
    required = {0: 4, 3: 4, 4: 4}

    solution = solve(top, bottom, required)
    print(f"Rotate top {solution[0]} times, rotate bottom {solution[1]} times.")


if __name__ == "__main__":
    main()
