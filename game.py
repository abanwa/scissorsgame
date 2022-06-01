import random

while True:
    choices = ["rock","paper","scissors"]

    computer = random.choice(choices)
    print(computer)

    player = None

    player = input(" choose one from (rock, paper, or scissors) : ").lower()

    while player not in choices:
        print("You have to choose from the given options ")
        player = input("Choose again (rock, paper, scissors :")

    if player == computer:
        print("Player :", player ," and Computer :", computer)
        print("Tie")
    
    elif player == "rock":
        if computer == "paper":
            print("Player :", player ," and Computer :", computer)
            print("You Lose!")
            break

        if computer == "scissors":
            print("Player :", player ," and Computer :", computer)
            print("You Win!")
            break

    elif player == "scissors":
        if computer == "rock":
            print("Player :", player ," and Computer :", computer)
            print("You Lose!")
            break

        if computer == "paper":
            print("Player :", player ," and Computer :", computer)
            print("You Win!")
            break

    elif player == "paper":
        if computer == "rock":
            print("Player :", player ," and Computer :", computer)
            print("You Win!")
            break

        if computer == "scissors":
            print("Player :", player ," and Computer :", computer)
            print("You Lose!")
            break
