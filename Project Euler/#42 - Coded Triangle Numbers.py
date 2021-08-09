from string import ascii_uppercase as alphabet


def istrianglenum(n):
    i = 1
    while 0.5*i*(i+1) < n:
        i += 1
    return 0.5*i*(i+1) == float(n)


def istriangleword(string):
    string = string.upper()
    values = [alphabet.index(c)+1 for c in string]
    return istrianglenum(sum(values))


with open("words.txt") as wordsfile:
    inputdata = [word.replace("\"", "") for word in wordsfile.readline().split(",")]

trianglewords = len([word for word in inputdata if istriangleword(word)])
print("Amount of 'triangular' words: %s" % trianglewords)
