from Routines.ask import ask
Sum = 0
Another = True
NumberList = []

while Another is True:
    Number = ask('Please enter a number.')
    Sum += int(Number)
    NumberList.append(Number)
    Continue = ask('Enter another number? (\'y\'/\'n\')')
    Another = 'y' in Continue.lower()

print('\nThe sum of your numbers: ')
for Index, Object in enumerate(NumberList):
    if Index == (len(NumberList) - 1):
        symbol = ''
    else:
        symbol = ' + '
    print(str(Object) + symbol)
print('= ' + str(Sum) + '\n')