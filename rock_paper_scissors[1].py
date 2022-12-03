# rock paper scissors
# future project -> build a telegram bot
import random as ra

print("commands:\n 'rock','paper','scissors'.  \n-type like this only\n to stop -'stop'\nto check scores say -'score'")
p1_score = 0
p2_score = 0


def rps(player_one_choice, player_two_choice):
    global p1_score
    global p2_score
    posibilities = ["you are thinking rock", "is that gonna be a paper", "gotta be honest i don't like you lad",
                    "im smelling scissors", "rocks right", "did you just pee in your pants?\n eww gross", "hmm"]
    if_won = ["its not over yet", "keep playing human i know where this is going", "wow"]
    won = ra.choice(if_won)
    if player_one_choice == "rock" and player_two_choice == "scissors":
        print("YOU WON", "\ncomputer: ", won)
        p1_score += 1
    elif player_one_choice == "paper" and player_two_choice == "rock":
        print("YOU WON", "\ncomputer: ", won)
        p1_score += 1
    elif player_one_choice == "scissors" and player_two_choice == "paper":
        print("YOU WON", "\ncomputer: ", won)
        p1_score += 1
    elif player_one_choice == "paper" and player_two_choice == "paper":
        print("DRAW\n", "computer:", ra.choice(posibilities))
    elif player_one_choice == "scissors" and player_two_choice == "scissors":
        print("DRAW\n", "computer:", ra.choice(posibilities))
    elif player_one_choice == "rock" and player_two_choice == "rock":
        print("DRAW\n", "computer:", ra.choice(posibilities))
    elif player_one_choice == "score":
        print("player one: ", p1_score)
        print("player two: ", p2_score)
    elif player_one_choice == "stop":
        print("bye mate")
    else:
        bull = ["suck deez nuts", "i smell something burning", "looser on ile 3", "you want some garlic bread?",
                "gotta be honest you suck mate", "i dont like you lad"]
        print("YOU LOST\n", "computer: ", ra.choice(bull))
        p2_score += 1


while True:
    p1_choice = input("player: ")
    choices = ["rock", "paper", "scissors"]
    if p1_choice == "stop":
        duche = ["die human", "bye mate", "you should kill yourself", "hate you lad"]
        print("computer:", ra.choice(duche))
        break
    p2_choice = ra.choice(choices)
    print("computer:", p2_choice)

print("hello world")