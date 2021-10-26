from random import randint

# add player and computer lives
playerLives = 5
computerLives = 5

# save the player as a variable called player
# the value of the player will be one of three choices to type (input)
player= input("choose rock, paper or scissors: ")

print("player choose: " + player)

# an array is just a container. it hholds multiple values in a 0-based index
#you can store anything in an array and retireve it later. arrays have square bracket notation
choices = ["rock", "paper" , "scissors"]
player = False

computer = choices[randint(0,2)]

print("computer choose: " + computer)
# define a win/lose function, make it loop
def winorlose(status):
    print("You " + status + "! would you like to play again?")
    choice = input(" Y / N?")

    global playerLives
    global computerLives
    global player

    if choice == "n":
        print("better luck next time!")
        exit()
    else:
        # rest and restart game
        #playerLives = 5
        #computerLives = 5
        #player = False


    while player is False:

 if (computer == player):
    print("tie! try again!")

 elif (player == "rock"):
    if (computer == "paper"):
        print("you lose!")
        playerLives = playerLives - 1
    else:
        print("you win!")
        computerLives = computerLives - 1

 elif (player == "paper"):
    if (computer == "scissors"):
        print("you lose!")
        playerLives = playerLives - 1
    else:
        print("you win!")
        computerLives = computerLives - 1

 elif (player == "scissors"):
    if (computer == "rock"):
        print("you lose!")
        playerLives = playerLives - 1
    else:
        print("you win!")
        computerLives = computerLives - 1

 print("player life count: "+ str(playerLives))
 print("computer life count: "+ str(computerLives))


    if playerLives == 0:
     #call the winorlose function here
     winorlose("lost")
    print("you lost! would you like to play again?")
    choice = input(" Y / N?")

    if choice == "n":
        print("better luck next time!")
        exit()
    else:
        # rest and restart game
            playerLives = 5
            computerLives = 5
            player = False

    elif computerLives == 0:
        print("you won! would you like to play again?")
        choice = input (" Y / N?")

    if choice == "n":
            print("better luck next time!")
            exit()
    else:
        # rest and restart game
            playerLives = 5
            computerLives = 5
            player = False

    player= False