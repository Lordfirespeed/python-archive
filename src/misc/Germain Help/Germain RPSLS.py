import random

endgame = False


def Simplify(A):
    global Usersimple
    if A == "Rock" or A == "rock" or A == "R" or A == "r":  # {A == "Rock" or A == "rock"} can be simplified to {A.lower() == "rock"}
        Usersimple = 1
    elif A == "Paper" or A == "paper" or A == "P" or A == "p":
        Usersimple = 2
    elif A == "Scissors" or A == "Scissor" or A == "scissors" or A == "scissor":  # total expression can be simplified to {'scissor' in A.lower()}
        Usersimple = 3
    elif A == "Lizard" or A == "lizard" or A == "L" or A == "l":
        Usersimple = 4
    elif A == "Spock" or A == "spock":
        Usersimple = 5
    else:
        Usersimple = 6
    return Usersimple
# On a whole, this function could be replaced by a dictionary. E.g. Paper + Rock only would be:
# (including curlies) simplify = {"rock": 1, "r": 1, "paper": 2, "p": 2}
# you'd want to reference it something like " simplify[A.lower()] " (where the .lower() casts it to lowercase so you don't have to have "Rock" or "Paper" in the dictionary)


def UIPlayer(A):
    if A == 1:
        print()
        print("Player: Rock")
    elif A == 2:
        print()
        print("Player: Paper")
    elif A == 3:
        print()
        print("Player: Scissors")
    elif A == 4:
        print()
        print("Player: Lizard")
    elif A == 5:
        print()
        print("Player: Spock")
# Again, this can be simplified to a dictionary - 
# UIPlayer = {1: "Rock", 2: "Paper"...}
# If you were being snazzy, you could even change your 'Rock' number to 0 (and the others accordingly) and just use a list ;)


def UIComputer(B):
    if B == 1:
        print("Computer: Rock")
    elif B == 2:
        print("Computer: Paper")
    elif B == 3:
        print("Computer: Scissors")
    elif B == 4:
        print("Computer: Lizard")
    elif B == 5:
        print("Computer: Spock")
# DICTIONARY! or a list. 
        
        
def Rockcheck():
    global User_Wins  # Even if they have a dud value, these should be defined above the function defition, in the global scope, prior to reference.
    global Computer_Wins
    global Ties
    global Computer_choice

    if Computer_choice == 1:
        Ties += 1
        print("Tie")
        return ""  # Return statements don't require parentheses () because they are not functions like print() - {return ""} is fine, I've edited this
    elif Computer_choice == 2:
        Computer_Wins += 1
        print("You Lost")
        return ""
    elif Computer_choice == 3:
        User_Wins += 1
        print("You Won")
        return ""
    elif Computer_choice == 4:
        User_Wins += 1
        print("You Won")
        return ""
    elif Computer_choice == 5:
        Computer_Wins += 1
        print("You Lost")
        return ""


def Papercheck():
    global User_Wins
    global Computer_Wins
    global Ties
    global Computer_choice

    if Computer_choice == 1:
        User_Wins += 1
        print("You Won")
        return ""
    elif Computer_choice == 2:
        Ties += 1
        print("Tie")
        return ""
    elif Computer_choice == 3:
        Computer_Wins += 1
        print("You Lost")
        return ""
    elif Computer_choice == 4:
        Computer_Wins += 1
        print("You Lost")
        return ""
    elif User_choice == 5:  # I believe this is a copy paste(?) error - shouldn't this be 'Computer_choice' ?
        User_Wins += 1
        print("You Won")
        return ""


def Scissorscheck():
    global User_Wins
    global Ties
    global Computer_Wins

    if Computer_choice == 1:
        Computer_Wins += 1
        print("You Lost")
        return ""
    elif Computer_choice == 2:
        User_Wins += 1
        print("You Won")
        return ""
    elif Computer_choice == 3:
        Ties += 1
        print("Tie")
        return ""
    elif Computer_choice == 4:
        User_Wins += 1
        print("You Won")
        return ""
    elif Computer_choice == 5:
        Computer_Wins += 1
        print("You Lost")
        return ""


def Lizardcheck():
    global User_Wins
    global Computer_Wins
    global Ties
    global Computer_choice

    if Computer_choice == 1:
        Computer_Wins += 1
        print("You Lost")
        return ""
    elif Computer_choice == 2:
        User_Wins += 1
        print("You Won")
        return ""
    elif Computer_choice == 3:
        Computer_Wins += 1
        print("You Lost")
        return ""
    elif Computer_choice == 4:
        Ties += 1
        print("Tie")
        return ""
    elif Computer_choice == 5:
        User_Wins += 1
        print("You Won")
        return ""


def Spockcheck():
    global User_Wins
    global Computer_Wins
    global Ties
    global Computer_choice

    if Computer_choice == 1:
        User_Wins += 1
        print("You Won")
        return ""
    elif Computer_choice == 2:
        Computer_Wins += 1
        print("You Lost")
        return ""
    elif Computer_choice == 3:
        User_Wins += 1
        print("You Won")
        return ""
    elif Computer_choice == 4:
        Computer_Wins += 1
        print("You Lost")
        return ""
    elif Computer_choice == 5:
        Ties += 1
        print("Ties")
        return ""

# OK, wow. Long-winded. Dictionaries would really have helped you here. Instead of doing 5 functions, you could do a dictionary with nested lists to show what wins + loses to what: e.g.
# whoWon = {1: [3, 4], 2: [1, 5]...}
# you could then do something with the choices, like this:
# First check for a draw. "if computerChoice == playerChoice: ... draw()" etc.
# Otherwise, evaluate who won.
# playerWon = computerChoice in whoWon[playerChoice]
# if the playerchoice was 2 (paper) and the computerchoice was 5 (spock), then the literal expression would be
# playerWon = 5 in [1, 5] (which is true, so the player won)
# if the computerChoice was not in [1, 5] then it was either 3 or 4 (not 2 as we checked for a draw) and the computer wins, so playerWon will be false.
# Then you can do something like
#   if playerWon:
#       print("You Won!")
#       player_Wins += 1


def original():
    global User_Wins
    global Computer_Wins
    global Ties
    global Computer_choice
    global Usersimple
    User_Wins = 0
    Computer_Wins = 0
    Ties = 0
    repeat = True

    while repeat == True:  # this is the same as writing 'while repeat:'. This kind of thing is what is referred to as 'pythonian' as it's more concise whilst being, occasionally, less readable :)
        print("Rock, Paper or Scissors?")
    
        User_choice = input()
        Computer_choice = random.randint(1, 3)  # It's good practise to put spaces between arguments to functions i.e (1, 3) not (1,3)

        Simplify(User_choice)

        if Usersimple == 4 or Usersimple == 5 or Usersimple == 6:  # Removed redundant parentheses. Original line: {if (Usersimple) == 4 or (Usersimple) == 5 or (Usersimple) == 6:}
            print("Invalid Input, Please Use an Accepted Input")

        UIPlayer(Usersimple)
        UIComputer(Computer_choice)
        print()
        
        if Usersimple == 1:  # Removed redundant parentheses
            print(Rockcheck())
        elif Usersimple == 2:
            print(Papercheck())
        elif Usersimple == 3:
            print(Scissorscheck())

        print("Player:%d; Computer:%d; Draws:%d" % (User_Wins, Computer_Wins, Ties))  # whitespace between arguments
        print("Another round?")
        repeat_check = input()

        if repeat_check == "Yes" or repeat_check == "yes" or repeat_check == "Y" or repeat_check == "y":  # "y" in repeat_check.lower()
            print()
        else:
            repeat = False
        
    print("See you later then")  # this needs a comma. -Yours, Grammar Hitler
    print("***Final Score***")
    print("Player: %d; Computer: %d; Draws: %d" % (User_Wins, Computer_Wins, Ties))


def additional():
    global User_Wins
    global Computer_Wins
    global Ties
    global Computer_choice
    global Usersimple
    User_Wins = 0
    Computer_Wins = 0
    Ties = 0
    repeat = True

    while repeat == True:  # while repeat:
        print("Rock, Paper, Scissors, Lizard or Spock?")
    
        User_choice = input()
        Computer_choice = random.randint(1,5)

        Simplify(User_choice)

        if Usersimple == 6:
            print("Invalid Input, Please Use an Accepted Input")

        UIPlayer(Usersimple)
        UIComputer(Computer_choice)
        print()
        
        if Usersimple == 1:
            print(Rockcheck())
        elif Usersimple == 2:
            print(Papercheck())
        elif Usersimple == 3:
            print(Scissorscheck())
        elif Usersimple == 4:
            print(Lizardcheck())
        elif Usersimple == 5:
            print(Spockcheck())
    
        print("Player:%d; Computer:%d; Draws:%d" % (User_Wins, Computer_Wins, Ties))
        print("Another round?")
        repeat_check = input()

        if repeat_check == "Yes" or repeat_check == "yes" or repeat_check == "Y" or repeat_check == "y":
            print()
        else:
            repeat = False
        
    print("See you later then")
    print("***Final Score***")
    print("Player:%d; Computer:%d; Draws:%d" % (User_Wins,Computer_Wins,Ties))


while endgame == False:  # while endgame:
    print()
    print("Would you like to play 'Rock, Paper, Scissors' or 'Rock, Paper, Scissors, Lizard, Spock'")
    print("Pick 1 or 2 otherwise type 'No' or a variant of it")

    Answer = input()

    if Answer == "1":
        print()
        original()
    elif Answer == "2":
        print()
        additional()
    elif Answer == "NO" or Answer == "No" or Answer == "no" or Answer == "N" or Answer == "n":
        endgame = True
    else:
        print("Invalid Input, Please Use an Accepted Input")
print("Terminated")
