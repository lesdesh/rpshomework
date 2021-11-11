from gameComponents import gameVars


def winorlose(status):
    print("you " + status)

    choice = input("do you want to play again? y/n: ")

    if choice == "n":
        print("٭(ෆ˙ᵕ˙ෆ)٭٭٭٭Thanks for playing! See ya!٭٭٭٭(ෆ˙ᵕ˙ෆ)٭")
        exit()
    elif choice == "y":
        print("٭ಥ_ಥ٭٭٭I'll win this time!٭٭٭ಥ_ಥ٭")
        gameVars.playerLives = 5
        gameVars.computerLives = 5
        gameVars.player = False
