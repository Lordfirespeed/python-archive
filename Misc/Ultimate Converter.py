def startup(message):
    msglength = (len(message) + 2)
    print('-' * msglength)
    print(' ' + message + ' ')
    print('-' * msglength)
    print()


def ask(message):
    print(message)
    this = input('> ')
    print()
    return this


def output(amount, unit, amountMiles):
    global valueInList
    global distances
    global temperature
    print(str(amount) + ' ' + unit + ' is equal to: ')
    print(str(amountMiles * 1) + ' Miles')
    print(str(amountMiles * 1760) + ' Yards')
    print(str(amountMiles * 5280) + ' Feet')
    print(str(amountMiles * 63360) + ' Inches')
    print(str(amountMiles * 1.609344) + ' Kilometres')
    print(str(amountMiles * 1609.344) + ' Metres')
    print(str(amountMiles * 16093.44) + ' Decimetre')
    print(str(amountMiles * 160934.4) + ' Centimetre')
    print(str(amountMiles * 1609344) + ' Millimetre')
    print()


startup('ULTIMATE CONVERTER')

startInput = ask('Please enter an amount and a unit in the format \'Amount - Space - Unit \'.')
amount, fromUnit = startInput.split(' ')
amount = int(amount)

distances = ['Mile', 'Yard', 'Foot', 'Inch', 'Kilometre', 'Metre', 'Decimetre', 'Centimetre', 'Millimetre']
distancesAbbrev = ['Mi', 'Ya', 'F', 'In', 'Km', 'M', 'Dm', 'Cm', 'Mm']

temperature = ['Celcius', 'Fahrenheit']
temperatureAbbrev = ['C', 'F']

valueNo = 0
for value in distancesAbbrev:
    if fromUnit.lower() == value.lower():
        valid = True
        valueInList = (valueNo)
        fromType = ('distance')
    valueNo += 1

if fromType == 'distance':
    print(distances[valueInList])
    if (distances[valueInList]) == (distances[0]):
        amountMiles = (amount * 1)
        unit = 'Mile(s)'
    if (distances[valueInList]) == (distances[1]):
        amountMiles = (amount * 0.00056818)
        unit = 'Yard(s)'
    if (distances[valueInList]) == (distances[2]):
        amountMiles = (amount * 0.00018939)
        unit = 'Foot / Feet'
    if (distances[valueInList]) == (distances[3]):
        amountMiles = (amount * 0.00001578)
        unit = 'Inch(es)'
    if (distances[valueInList]) == (distances[4]):
        amountMiles = (amount * 0.62137119)
        unit = 'Kilometre(s)'
    if (distances[valueInList]) == (distances[5]):
        amountMiles = (amount * 0.00062137)
        unit = 'Metre(s)'
    if (distances[valueInList]) == (distances[6]):
        amountMiles = (amount * 0.000062137)
        unit = 'Decimetre(s)'
    if (distances[valueInList]) == (distances[7]):
        amountMiles = (amount * 0.0000062137)
        unit = 'Centimetre(s)'
    if (distances[valueInList]) == (distances[8]):
        amountMiles = (amount * 0.00000062137)
        unit = 'Millimetre(s)'

    output(amount, unit, amountMiles)
 
else:
    print('Unit not recognised.')
