from random import randint
from gameComponents import winLose, gameVars, score

# set up our game loop so that we can keep playing and not exit
while gameVars.player is False:
    gameVars.player = input("Choose your weapon: rock, paper or scissors: ")
    gameVars.computer = gameVars.choices[randint(0, 2)]

    heart_symbol = u'\u2764'

    print("player chose: " + gameVars.player)
    print("computer chose: " + gameVars.computer)

    score.tie()
    score.rock()
    score.paper()
    score.scissors()


    print("player life count: " + heart_symbol * gameVars.playerLives + str(gameVars.playerLives))
    print("computer life count: " + heart_symbol * gameVars.computerLives + str(gameVars.computerLives))

    if gameVars.playerLives == 0:
        winLose.winorlose("lost!")

    elif gameVars.computerLives == 0:
        winLose.winorlose("won!")

    gameVars.player = False
