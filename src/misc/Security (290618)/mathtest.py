import random
from math import sqrt

import encoding
from usercommands import login, logout

global operators
operators = ["+", "-", "*", "/"]

def randomquestion(maxnum):
    global operators
    return generatequestion(maxnum, random.choice(operators))
    
def generatequestion(maxnum, operator):
    # Returns a list containing: a math question in the form of a printable string [0], and the answer as an int [1].
    if operator == "+":
        maxnum /= 2
        operanda = random.randint(2, maxnum)
        operandb = random.randint(2, maxnum)

    elif operator == "-":
        operanda = random.randint(2, maxnum)
        operandb = random.randint(2, maxnum)
        operanda, operandb = max([operanda, operandb]), min([operanda, operandb])
        
    elif operator in "*/":
        maxnum = int(sqrt(maxnum))
        operanda = random.randint(2, maxnum)
        operandb = random.randint(2, maxnum)
        if operator == "/":
            operanda *= operandb

    else:
        operanda = random.randint(2, maxnum)
        operandb = random.randint(2, maxnum)

    question = (str(operanda) + " " + str(operator) + " " + str(operandb))
    answer = eval(question)
    return [question, int(answer)]

def quiz(maxnumber, qtype="random", qamount=10):
    global operators
    if (not qtype in operators) and (not qtype in "random"):
        return False
    elif qtype in "random":
        questions = [randomquestion(maxnumber) for x in range(qamount)]
    elif qtype in operators:
        questions = [generatequestion(maxnumber, qtype) for x in range(qamount)]
        
    answerscorrect = []
    useranswers = []
    actualanswers = []
    
    for question in questions:
        useranswer = input(question[0] + " = ")
        answer = question[1]
        useranswers.append(int(useranswer))
        actualanswers.append(question[1])
        answerscorrect.append(bool(answer == int(useranswer)))

    return [answerscorrect, useranswers, actualanswers]
            
userloggedin = False
while not userloggedin:
    userloggedin = True
    print("You are not logged in.\nPlease enter a valid UserSYS username and password, comma separated.\n")
    try:
        username, password = input("> ").split(",")
        username = username.strip()
        password = password.strip()
    except ValueError:
        print("Invalid comma separation. Did you supply too many values?")
        userloggedin = False
    if userloggedin:
        tryuser = login(username, password)
        print(tryuser[1])
        if tryuser[0]:
            userloggedin = username.title()
        else:
            userloggedin = False
        
print()

mainloop = True
while mainloop:
    userinput = "> "
    if "settings" in userinput.lower():
        print("Enter your preferred difficulty settings.")
        print("Use the format 'maximum number, question type, question amount'.")
        print("Example: '100, +, 5'.")
        settingsinput = input("> ")

    elif "quiz" in userinput.lower():
        print("oof")
    
