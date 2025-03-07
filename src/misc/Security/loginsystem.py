logindict = {}

def refresh():
    global logindict
    userfile = "data/userfile.txt"
    logindict = {}
    with open(userfile) as file:
        for line in file.readlines():
            line = line.rstrip()
            data = line.split(", ")
            logindict[data[0]] = data[1]

def login(user, password):
    global logindict
    if not user in logindict:
        return False
    else:
        if logindict[user] == password:
            return True
        else:
            return False

refresh()
