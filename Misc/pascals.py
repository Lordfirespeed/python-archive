from math import factorial


def next_list(current_list):
    shouldbelen = len(current_list) + 1
    
    if current_list[0] != 0:
        current_list.insert(0, 0)
    if current_list[-1] != 0:
        current_list.append(0)
        
    return_next_list = []
    for index in range(1, shouldbelen + 1):
        return_next_list.append(current_list[index - 1] + current_list[index])
        
    return return_next_list


def pascal_line(line_index):
    if line_index == 0:
        return [1]
    else:
        prev_list = pascal_line(line_index - 1)
        return next_list(prev_list)


def choices(total, amount):
    try:
        possible = ((factorial(total)) / (factorial(amount) * factorial(total - amount)))
    except ZeroDivisionError:
        possible = 1
    return possible


def other_pascal_line(line_index):
    length = line_index + 1
    pascal_line_list = []
    for index in range(length):
        pascal_line_list.append(int(choices(line_index, index)))
    return pascal_line_list

