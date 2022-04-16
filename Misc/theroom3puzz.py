import itertools

options = [["+2", "+8"], ["x2", "x5"], ["+4", "+7"], ["+3", "+12"], ["-5", "-17"], ["+2", "+9"]]
target = 30

for selections in itertools.product(*options):
    accumulator = 0
    for command in selections:
        if command[0] == "+":
            accumulator += int(command[1:])
        elif command[0] == "-":
            accumulator -= int(command[1:])
        elif command[0] == "x":
            accumulator *= int(command[1:])
    if accumulator == target:
        print(selections)
        break
