from string import ascii_lowercase as alphabet
thing = "znkvgyycux"
print("".join([alphabet[25-alphabet.index(c)] for c in thing]))
