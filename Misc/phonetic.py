phonetics = {
    "A": "Alfa",
    "B": "Bravo",
    "C": "Charlie",
    "D": "Delta",
    "E": "Echo",
    "F": "Foxtrot",
    "G": "Golf",
    "H": "Hotel",
    "I": "India",
    "J": "Juliett",
    "K": "Kilo",
    "L": "Lima",
    "M": "Mike",
    "N": "November",
    "O": "Oscar",
    "P": "Papa",
    "Q": "Quebec",
    "R": "Romeo",
    "S": "Sierra",
    "T": "Tango",
    "U": "Uniform",
    "V": "Victor",
    "W": "Whiskey",
    "X": "X-Ray",
    "Y": "Yankee",
    "Z": "Zulu"
    }

def phonetify(input_str: str):
    global phonetics
    san_input = "".join([c.upper() for c in input_str if c.upper() in phonetics.keys()])
    return " ".join([phonetics[c] for c in san_input])

if __name__ == "__main__":
    le_input = input("Provide input:\n> ")
    print(phonetify(le_input))
    input()
