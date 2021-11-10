from random import randint
from gameComponents import winLose, gameVars

# set up our game loop so that we can keep playing and not exit
while gameVars.player is False:
    gameVars.player = input("Choose your weapon: rock, paper or scissors: ")
    gameVars.computer = gameVars.choices[randint(0, 2)]

    heart_symbol = u'\u2764'

    print("player chose: " + gameVars.player)
    print("computer chose: " + gameVars.computer)

    if gameVars.computer == gameVars.player:
        # tie - nothing else to compare, so it'll exit
        print("==========")
        print("tie! try again")
        print("==========")

    elif gameVars.player == "rock":
        if gameVars.computer == "paper":
            print("==========")
            print("you lose!")
            print("==========")
            gameVars.playerLives = gameVars.playerLives - 1 
        else:
            print("==========")
            print("you win!")
            print("==========")
            gameVars.computerLives = gameVars.computerLives - 1

    elif gameVars.player == "paper":
        if gameVars.computer == "scissors":
            print("==========")
            print("you lose!")
            print("==========")
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            print("==========")
            print("you win!")
            print("==========")
            gameVars.computerLives = gameVars.computerLives - 1

    elif gameVars.player == "scissors":
        if gameVars.computer == "rock":
            print("==========")
            print("you lose!")
            print("==========")
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            print("==========")
            print("you win!")
            print("==========")
            gameVars.computerLives = gameVars.computerLives - 1

    print("player life count: " + heart_symbol * gameVars.playerLives + str(gameVars.playerLives))
    print("computer life count: " + heart_symbol * gameVars.computerLives + str(gameVars.computerLives))

    if gameVars.playerLives == 0:
        winLose.winorlose("lost")

    elif gameVars.computerLives == 0:
        winLose.winorlose("won")

    gameVars.player = False
