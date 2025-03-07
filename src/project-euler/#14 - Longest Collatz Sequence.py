def getsequence(integer):
    sequence = [int(integer)]
    while integer != 1:
        if integer % 2 == 0:
            integer /= 2
        else:
            integer *= 3
            integer += 1
        sequence.append(integer)
    return sequence


maxlength = 0
maxlengthindex = 0
for index in range(1, 1_000_000):
    sequence = getsequence(index)
    if len(sequence) > maxlength:
        maxlength = len(sequence)
        maxlengthindex = index
    if index % 10000 == 0:
        print("Hit index " + str(index))
print(maxlengthindex, maxlength)
