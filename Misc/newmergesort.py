def bubblesort(listnums):
    sortedlist = list(listnums)
    totalswaps = 0
    swaps = 1
    while swaps != 0:
        swaps = 0
        for index, number in enumerate(sortedlist[:-1]):
            if number > sortedlist[index+1]:
                sortedlist[index], sortedlist[index+1] = sortedlist[index+1], sortedlist[index]
                swaps += 1
    return sortedlist

def mergesort(listnums):
    length = len(listnums)
    if length <= 1:
        return listnums
    half = int(length / 2)
    leftstack = mergesort(listnums[:half])
    rightstack = mergesort(listnums[half:])
    sortedlist = []
    while len(leftstack) > 0 and len(rightstack) > 0:
        if leftstack[0] <= rightstack[0]:
            sortedlist.append(leftstack.pop(0))
        else:
            sortedlist.append(rightstack.pop(0))
    for remaining in leftstack:
        sortedlist.append(remaining)
    for remaining in rightstack:
        sortedlist.append(remaining)
    return sortedlist

def buckets(listnums, index):
    listnumstrs = list([str(num) for num in listnums])
    buckets = [[], [], [], [], [], [], [], [], [], []]
    for value in listnumstrs:
        buckets[int(value[index])].append(int(value))
    return list([bucket for bucket in buckets if bucket != []])

def redixsort(listnums):
    listnumstrs = list([str(num) for num in listnums])
    maxlength = max(list([len(val) for val in listnumstrs]))
