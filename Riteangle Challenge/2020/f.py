squares = [1]


def get_possible(b_index):
    global squares
    return [squares[b_index] - squares[c_index] for c_index in range(b_index)]


ways_of_making = {}


def add_square():
    global squares
    global ways_of_making
    squares.append((len(squares)+1)**2)
    nums_made = get_possible(len(squares)-1)
    for num in nums_made:
        if num % 2 != 0:
            if num not in ways_of_making.keys():
                ways_of_making[num] = 0
            ways_of_making[num] += 1


a = None
while not a:
    if list(ways_of_making.values()).count(4) >= 3:
        break
    else:
        add_square()


possible_a = []

for num, ways in ways_of_making.items():
    if ways == 4:
        possible_a.append(num)

print(f"a = {min(possible_a)}")
