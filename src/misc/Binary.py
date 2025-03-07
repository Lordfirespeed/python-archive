number = int(input('To number: '))
for x in range(0, number + 1):
    length = len(str(2**x))
    characters = []
    for i in range(0, length):
        if i % 3 == length % 3:
            characters.append(' ')
        characters.append(str(2**x)[i])
    
    message = (str(x) + ' bits; 2^' + str(x) + '; ' + (''.join(characters)).strip())
    if x == 1:
        message += '    <- Bit'
    elif x == 4:
        message += '    <- Nibble (4 Bits)'
    elif x == 8:
        message += '    <- Byte (8 Bits)'
    print(message)
        
