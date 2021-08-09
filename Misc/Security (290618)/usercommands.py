from random import randint
import encoding

loginlist = []
userfile = "data/loginsfile.txt"
groupsfile = "data/groupsfile.txt"
validstatus = ["admin", "teacher", "staff", "student"]
userperms = "none"
userloggedin = False

def refresh():
# admin
    global loginlist
    global userfile
    try:
        with open(userfile) as file:
            for line in file.readlines():
                line = (line.rstrip())
                keyindex = line.index(": ")
                key = int(line[:keyindex])
                encodeddata = line[(keyindex + 2):]
                decodeddata = encoding.decode(encodeddata, key)
                data = decodeddata.split(", ")
                loginlist.append(data)
        commands = ["pass"]
        return [True, "Successfully refreshed system.", commands]
    except:
        return [False, "Failed to refresh.", commands ]

def login(user, password):
# none, student, staff, teacher, admin
    global loginlist
    global userloggedin
    global userperms
    found = False
    foundindex = 0
    for index, thing in enumerate(loginlist, 0):
        if thing[0] == user.title():
            found = True
            foundindex = index
            break
    if not found:
        commands = ["pass"]
        return [False, ("User '" + user.title() + "' doesn't exist."), commands]
    else:
        if loginlist[index][1] == password:
            userloggedin = user.title()
            userperms = loginlist[index][2]
            commands = ["userloggedin = usercommands.userloggedin", "userperms = usercommands.userperms"]
            return [True, ("Welcome, " + user.title() + ". You have " + userperms.title() + " permissions."), commands]
        else:
            commands = ["pass"]
            return [False, ("Incorrect password for user " + user.title() + "."), commands]

def logout():
# none, student, staff, teacher, admin
    global userloggedin
    global userperms
    userloggedin = False
    userperms = "none"
    commands = ["userloggedin = usercommands.userloggedin", "userperms = usercommands.userperms"]
    return [True, "Successfully logged out.", commands]

def passwordelegible(password):
# 
    uppercase = False
    uppercase = bool(sum(char.isupper() for char in password))
    if not uppercase:
        return ("You need to have a minimum of one uppercase letter in your password.")
    numbers = False
    numbers = bool(sum(char.isdigit() for char in password) - 1)
    if not numbers:
        return ("You need to have a minimum of two numbers in your password.")
    return True
    
def createlogin(user, password, status):
# admin, teacher
    global userfile
    global loginlist
    global validstatus
    commands = ["pass"]
    if user.lower() in loginlist:
        return [False, "Username taken.", commands]
    check = passwordelegible(password)
    if check != True:
        return [False, check, commands]
    if not status in validstatus:
        return [False, "Invalid status.", commands]
    userdata = [user.title(), password, status.lower()]
    userdata = ", ".join(userdata)
    key = randint(0, 255)
    encodeddata = encoding.encode(userdata, key)
    with open(userfile, "a") as file:
        file.write(str(key) + ": " + encodeddata + "\n")
    return [True, ("Successfully created user " + user.title() + " with " + status.title() + " priveleges."), commands]
    refresh()

def creategroup(subject, groupname):
# admin
    global groupsfile
    commands = ["pass"]
    with open(groupsfile) as groupsdata:
        grouptext = (subject + " - " + groupname).title()
        found = False
        for index, line in enumerate(groupsdata.readlines(), 0):
            line = line.rstrip()
            if line[:line.index(":")].title().rstrip() == grouptext.rstrip():
                found = True
                break
    if found:
        return [False, ("Group " + grouptext + " already exists."), commands]
    else:
        with open(groupsfile, "a") as groupswrite:
            groupswrite.write(grouptext + ": \n")
        commands = ["pass"]
        return [True, ("Group " + grouptext + " successfully created."), commands]

def delgroup(subject, groupname):
# admin
    global groupsfile
    commands = ["pass"]
    grouptext = (subject + " - " + groupname).title()
    with open(groupsfile) as groupsdata:
        found = False
        foundindex = 0
        for index, line in enumerate(groupsdata.readlines(), 0):
            line = line.rstrip()
            if line[:line.index(":")].title().rstrip() == grouptext.rstrip():
                found = True
                foundindex = index
                break
    if found:
        with open(groupsfile, "r+") as groupwrite:
            lines = groupwrite.readlines()
            del lines[foundindex]
            groupwrite.seek(0)
            groupwrite.truncate()
            groupwrite.writelines(lines)
        return [True, ("Successfully removed group " + grouptext + "."), commands]
    else:
        return [False, ("Failed to remove group " + grouptext + "."), commands]
    
def groupadd(subject, groupname, user):
# admin, teacher
    global groupsfile
    global loginlist
    commands = ["pass"]
    grouptext = (subject + " - " + groupname).title()
    with open(groupsfile) as groupsdata:
        found = False
        foundindex = 0
        for index, line in enumerate(groupsdata.readlines(), 0):
            line = line.rstrip()
            if line[:line.index(":")].title().rstrip() == grouptext.rstrip():
                found = True
                foundindex = index
                break
    if not found:
        return [False, ("Group " + grouptext + " not found."), ["pass"]]
    else:
        founduser = False
        for userdata in loginlist:
            if userdata[0].title() == user.title():
                founduser = True
                break
        if not founduser:
            return [False, ("User " + user.title() + " does not exist."), ["pass"]]
        else:
            with open(groupsfile, "r+") as groupswrite:
                lines = groupswrite.readlines()
                if user.title() in lines[foundindex]:
                    return [False, ("User " + user.title() + " already in group " + grouptext + "."), ["pass"]]
                else:
                    lines[foundindex] = lines[foundindex].rstrip()
                    if not lines[foundindex][-1] == ":":
                        lines[foundindex] += ", "
                    else:
                        lines[foundindex] += " "
                    lines[foundindex] += user.title() + "\n"
                    groupswrite.seek(0)
                    groupswrite.truncate()
                    groupswrite.writelines(lines)
                    return [True, ("Successfully added user " + user.title() + " to group " + grouptext + "."), ["pass"]]

def groupremove(subject, groupname, user):
# admin, teacher
    global groupsfile
    global loginlist
    commands = ["pass"]
    grouptext = (subject + " - " + groupname).title()
    with open(groupsfile) as file:
        found = False
        foundindex = 0
        for index, line in enumerate(file.readlines(), 0):
            line = line.rstrip()
            if line[:line.index(":")].title().rstrip() == grouptext.rstrip():
                found = True
                foundindex = index
                break
    if not found:
        return [False, ("Group " + grouptext + " not found."), ["pass"]]
    else:
        with open(groupsfile, "r+") as groupswrite:
            lines = groupswrite.readlines()
            groupline = lines[foundindex].strip()
            if not user.title() in groupline:
                return [False, ("User " + user.title() + " not in group " + grouptext + "."), commands]
            else:
                if groupline[groupline.index(user) -2] == ":":
                    lines[foundindex] = groupline[:groupline.index(user)] + groupline[(groupline.index(user) + len(user) + 2):]
                else:
                    lines[foundindex] = groupline[:groupline.index(user) - 2] + groupline[(groupline.index(user) + len(user)):]
                lines[foundindex] += "\n"
                groupswrite.seek(0)
                groupswrite.truncate()
                groupswrite.writelines(lines)
                return [True, ("Successfully removed user " + user.title() + " from group " + grouptext + "."), ["pass"]]
                
refresh()
