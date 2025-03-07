from string import ascii_lowercase as alphabet

mapstring = alphabet * 2


def encode(string, key=1):
    return "".join([mapstring[alphabet.index(character.lower()) + key] for character in string])


def decode(string, key):
    return "".join([mapstring[alphabet.index(character.lower()) + 26 - key] for character in string])


def brutedecode(string):
    for index in range(1, 25):
        print(decode(string, index))

