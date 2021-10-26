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

computer = choices[randint(0,2)]

print("computer choose: " + computer)


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

