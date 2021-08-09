from string import printable
mapstring = printable + printable

def encode(string, key=10):
    global mapstring
    key %= int(len(mapstring) / 2)
    characterlist = []
    for character in string:
        index = mapstring.index(character)
        characterlist.append(mapstring[index + int(key)])
    # return "".join(characterlist)
    binarylist = []
    for character in characterlist:
        binchar = (bin(ord(character))[2:])
        if len(binchar) < 8:
            binchar = ("0" * (8 - len(binchar))) + binchar
        binarylist.append(binchar)
    connectedbinlist = "".join(binarylist)
    connectedbinlist = connectedbinlist.replace("0", "X")
    connectedbinlist = connectedbinlist.replace("1", "0")
    connectedbinlist = connectedbinlist.replace("X", "1")
    
    splitbinlist = [connectedbinlist[(8*x):(8*(x+1))] for x in range(int(len(connectedbinlist)/8))]
    hexlist = []
    for thing in splitbinlist:
        hexthing = hex(int(thing, 2))[2:]
        if len(hexthing) < 2:
            hexthing = "0" + hexthing
        hexlist.append(hexthing)
    hexstring = "".join(hexlist)
    outputlist = []
    for character in hexstring:
        index = mapstring.index(character)
        outputlist.append(mapstring[index + int(key)])
    return "".join(outputlist)
        
def decode(string, key=10):
    global mapstring
    key %= int(len(mapstring) / 2)
    hexlist = []
    for character in string:
        index = int(mapstring.index(character) + (len(mapstring) / 2))
        hexlist.append(mapstring[index - int(key)])
    # return "".join(hexlist)
    hexstring = "".join(hexlist)
    splithexstring = [hexstring[(2*x):(2*(x+1))] for x in range(int(len(hexstring)/2))]

    binarylist = []
    for thing in splithexstring:
        binthing = bin(int(thing, 16))[2:]
        if len(binthing) < 8:
            binthing = "0" * (8-len(binthing)) + binthing
        binarylist.append(binthing)
    connectedbinstring = "".join(binarylist)
    connectedbinstring = connectedbinstring.replace("0", "X")
    connectedbinstring = connectedbinstring.replace("1", "0")
    connectedbinstring = connectedbinstring.replace("X", "1")

    splitbinlist = [connectedbinstring[(8*x):(8*(x+1))] for x in range(int(len(connectedbinstring)/8))]
    characterlist = []
    for thing in splitbinlist:
        characterlist.append(chr(int(thing, 2)))

    outputlist = []
    for character in characterlist:
        index = int(mapstring.index(character) + (len(mapstring) / 2))
        outputlist.append(mapstring[index - int(key)])

    return "".join(outputlist)
    
