from string import printable
mapstring = printable + printable

def encode(string, key=10):
    global mapstring
    key %= int(len(mapstring) / 2)
    characterlist = []
    for character in string:
        index = mapstring.index(character)
        characterlist.append(mapstring[index + int(key)])
    return "".join(characterlist)
    
def decode(string, key=10):
    global mapstring
    key %= int(len(mapstring) / 2)
    outputlist = []
    for character in string:
        index = int(mapstring.index(character) + (len(mapstring) / 2))
        outputlist.append(mapstring[index - int(key)])
    return "".join(outputlist)
