import random

options = ("rock","paper","scissors")
running=True

while running:
   
    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("Enter a choice(rock,paper,scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie choice again please") 
    elif player == "rock" and computer == "scissors":
        print(" Congratulation you win")
    elif player == "paper" and computer == "rock":
        print(" Congratulation you win")
    elif player == "scissors" and computer == "paper" :
        print(" Congratulation you win")
    else: 
        print("Sorry you lose")

        if not input("Play Again ? (y/n): ").lower()=="y":
            running = False

print("Thanks for Playing,Bye.")