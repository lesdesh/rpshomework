from gameComponents import gameVars, winLose


def tie():
    if gameVars.computer == gameVars.player:
        print("٭٭٭٭٭Tie! Try again!٭٭٭٭٭")       

def rock():
    if gameVars.player == "rock":
        if gameVars.computer == "paper":
            print("٭٭٭٭٭You Lose!٭٭٭٭٭")
            gameVars.playerLives = gameVars.playerLives - 1
        if gameVars.computer == "scissors":
            print("٭٭٭٭٭You Win!٭٭٭٭٭")
            gameVars.computerLives = gameVars.computerLives - 1

def paper():
    if gameVars.player == "paper":
        if gameVars.computer == "scissors":
            print("٭٭٭٭٭You Lose!٭٭٭٭٭")
            gameVars.playerLives = gameVars.playerLives - 1
        if gameVars.computer == "rock":
            print("٭٭٭٭٭You Win!٭٭٭٭٭")
            gameVars.computerLives = gameVars.computerLives - 1


def scissors():
    if gameVars.player == "scissors":
        if gameVars.computer == "rock":
            print("٭٭٭٭٭You Lose!٭٭٭٭٭")
            gameVars.playerLives = gameVars.playerLives - 1
        if gameVars.computer == "paper":
            print("٭٭٭٭٭You Win!٭٭٭٭٭")
            gameVars.computerLives = gameVars.computerLives - 1

 