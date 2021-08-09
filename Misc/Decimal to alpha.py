from string import ascii_lowercase as alphabet
alphabet = " " + alphabet

outstring = ""
done = False
while not done:
    userinput = input("> ")
    if not userinput.isdecimal():
        done = True
    else:
        num = int(userinput)
        outstring = outstring + alphabet[num]
    print(outstring)
