numericalCode = 14026929
numberList = []
for number in range((len(str(numericalCode)))):
    numericalCodeInt = int(str(numericalCode)[number])
    numberList.append(numericalCodeInt * (8 - number))
    print(numericalCodeInt * (8 - number))
print(sum(numberList))
if ((sum(numberList) % 11) == 0):
    print('Accepted.')
else:
    print('Declined.')
