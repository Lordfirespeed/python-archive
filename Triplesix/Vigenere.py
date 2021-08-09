from string import ascii_lowercase as alphabet

mapstring = alphabet * 2


def caesarencode(string, key=1):
    return "".join([mapstring[alphabet.index(character.lower()) + key] for character in string])


mainmap = [[alphabet[index], [[alphabet[subindex], caesarencode(alphabet[subindex], index)] for subindex in range(0, 26)]] for index in range(0, 26)]
encodemap = [[key, dict(mapline)] for key, mapline in mainmap]
encodemap = dict(encodemap)
decodemap = [[key, dict([element[::-1] for element in mapline])] for key, mapline in mainmap]
decodemap = dict(decodemap)
# reference decodemap as decodemap[keycharacter][decodecharacter]


def encode(string, keystring):
    string = string.lower().replace(" ", "")
    keystring = keystring.lower().replace(" ", "")
    while len(keystring) < len(string):
        keystring = keystring * 2
    encoded = ""
    for index, character in enumerate(string):
        keycharacter = keystring[index]
        encoded += encodemap[keycharacter][character]
    return "".join(encoded)


def decode(string, keystring):
    spaces = [index for index in range(len(string)) if string[index] == " "]
    string = string.lower().replace(" ", "")
    keystring = keystring.lower().replace(" ", "")
    while len(keystring) < len(string):
        keystring = keystring * 2
    decoded = []
    for index, character in enumerate(string):
        keycharacter = keystring[index]
        decoded.append(decodemap[keycharacter][character])
    [decoded.insert(i, " ") for i in spaces]
    return "".join(decoded)


