def ask(message):
    print(message)
    thing = input('> ')
    return thing

moreResults = 'True'
resultNo = 1
resultList = []
while moreResults == 'True':
    newInput = ask('Test result #' + str(resultNo))
    resultList.append(newInput)
    moreResults = (ask('Reply \'True\' to continue to enter results')).title()
    resultNo += 1

total = 0
for thing in resultList:
    total += int(thing)

avg = total / len(resultList)

print('\nYour average score is ' + str(avg) + '.')

test = ask('Would you like to know if you passed? (y / n)')
if test == 'y':
    if avg >= 50:
        print('You passed!')
    else:
        print('You failed!')
else:
    print('OK, Goodbye!')
