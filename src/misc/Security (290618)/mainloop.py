import encoding
import simpleencode
import usercommands

global userloggedin
global userperms

checkfiles = ["usercommands"]

parentscripts = []
validfuncs = []
permissions = []
arglengths = []
for filescript in checkfiles:
    with open(filescript + ".py") as file:
        filelines = file.readlines()
        for index, line in enumerate(filelines, 1):
            line = line.rstrip()
            if line[0:3] == "def":
                permissions.append((filelines[index].rstrip()[2:]).split(", "))
                if "" in permissions[-1]:
                    permissions.remove(permissions[-1])
                else:
                    func = line[4:(line.index("(", 4))]
                    validfuncs.append(func.lower())
                    args = line[(line.index("(", 4) + 1):(line.index(")", 4))]
                    args = args.split(", ")
                    if "" in args:
                        arglengths.append(0)
                    else:
                        arglengths.append(len(args))
                    parentscripts.append(filescript)

userloggedin = False
userperms = "none"
print("Hello! Welcome to UserSYS. To login, try typing: 'login: username, password'.")
run = True
while run:
    try:
        print()
        userinput = input("> ")
        function = userinput[0:userinput.index(":")]
        if function in validfuncs:
            permsindex = validfuncs.index(function)
            if not userperms in permissions[permsindex]:
                # not permitted
                print("You aren't permitted to do that.")
                if not userloggedin:
                    print("You haven't logged in! To login, use the command: 'login: username, password'.")
                    print("If you don't have an account, ask an administrator to create you one!")
            else:
                # permitted
                args = userinput[(userinput.index(":")+1):]
                args = args.strip()
                args = args.split(",")
                arglength = len(args)
                for index, thing in enumerate(args, 0):
                    args[index] = "'" + thing.strip() + "'"
                args = ", ".join(args)
                if args == "''":
                    args = ""
                    arglength = 0

                if arglength != arglengths[permsindex]:
                    print("Incorrect arguments! Are they comma separated?")
                    
                else:
                    output = []
                    command = ("output = (" + parentscripts[index] + "." + function + "(" + args + "))")
                    # print(command)
                    exec(command)
                    print(output[1])
                    for endcommand in output[2]:
                        exec(endcommand)
                    
        else:
            # invalid command
            print("Sorry, command not recognised.")
    except ValueError:
        print("Invalid command format! You probably missed the colon.")
                
