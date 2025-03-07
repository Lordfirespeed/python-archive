Numbers = ['Dog', 'Cat', 'Horse', 'Goat', 'Lion', 'Zebra', 'Cow']

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
    print(result)
    return result

            
print(mergesort(Numbers))
