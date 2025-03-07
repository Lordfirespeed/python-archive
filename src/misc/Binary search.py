List = [90, 37, 18, 29, 10, 254, 27, 19, 47, 10, 582, 126, 28, 10]

def mergesort(List):
    result = []
    if len(List) < 2:
        return List
    mid = (int(len(List) / 2))
    Left = mergesort(List[:mid])
    Right = mergesort(List[mid:])
    LeftInt = 0
    RightInt = 0
    while LeftInt < len(Left) and RightInt < len(Right):
        # print(str(LeftInt), str(RightInt))
        if Left[LeftInt] < Right[RightInt]:
            result.append(Left[LeftInt])
            LeftInt += 1
        else:
            result.append(Right[RightInt])
            RightInt += 1
    result += Left[LeftInt:]
    result += Right[RightInt:]
    return result

List = mergesort(List)

def binarysearch(List, Search):
    if len(List) < 2:
        Bool = False
        if List[0] == Search:
            Bool = True
        return Bool

    Mid = int(len(List) / 2)
    if List[Mid] > Search:
        Var = binarysearch(List[:Mid], Search)
    else:
        Var = binarysearch(List[Mid:], Search)
    return Var
    
print(str(binarysearch(List, int(input('Enter a number: ')))))
