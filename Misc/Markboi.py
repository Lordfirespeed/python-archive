import random

songs = []
artists = []
username = "oof"

difficulty = {"h": 1, "m": 2, "e": 4}
points = {"h": 3, "m": 2, "e": 1}

play = True
while play:
    score = 0
    used = []
    chosendiff = input("How hard do you want it to be?(h,m,e): ")

    game = True
    while game:
        if len(used) == len(songs):
            game = False
            print("Oh no! You're out of songs, Game Over!")
            print("You got %s points." % score)
        else:
            number = random.randrange(len(songs))
            check = True
            while check:
                if number in used:
                    check = True
                    number = random.randrange(len(songs))
                else:
                    check = False
                used.append(number)
            userinput = input("Your song starts with %s and the artist is %s. What song is it?" % (songs[number][:difficulty[chosendiff]], artists[number]))

            if userinput.lower() == (songs[number]).lower():
                score += points[chosendiff]
                print("Correct! you have %s points and there are %s songs left." % (score, len(songs)-len(used)))
                check = True
            else:
                userinput = input("Incorrect,You have one more try: ")
                if userinput.lower() == (songs[number]).lower():
                    score += points[chosendiff]
                    print("Correct! you have %s points and there are %s songs left." % (score, len(songs)-len(used)))
                else:
                    print("That was wrong. The correct answer was %s." % songs[number])
                    game = False

    again = input("Do you want to play again? (y/n): ")
    play = "y" in again.lower()
