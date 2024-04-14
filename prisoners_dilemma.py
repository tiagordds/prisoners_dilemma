import random

ROUNDS = 50

current_round = 0


def player_1(choice: int) -> str:
    if choice == 1:
        return "Cooperate"
    if choice == 2:
        return "Defect"
    return "Isso aqui nunca deveria  acontecer, só coloquei porque to testando o typing"


def player_2(choice: int) -> str:
    if choice == 1:
        return "Cooperate"
    if choice == 2:
        return "Defect"
    return "Isso aqui nunca deveria  acontecer, só coloquei porque to testando o typing"


player_1_score = 0
player_2_score = 0


def player_score(p1: int, p2: int) -> tuple:
    global player_1_score
    global player_2_score
    player_1_score += p1
    player_2_score += p2
    return player_1_score, player_2_score


player_1_choice = []
player_2_choice = []

while current_round < ROUNDS:
    play1 = player_1(random.randint(1, 2))
    player_1_choice.append(play1)

    play2 = player_2(2)
    if current_round == 0:
        play2 = player_2(1)
    elif player_1_choice[-2] == "Cooperate":
        play2 = player_2(1)
    elif player_1_choice[-2] == "Defect":
        play2 = player_2(2)
    player_2_choice.append(play2)

    print(f"{play1} /////// {play2}")

    if play1 == "Cooperate" and play2 == "Cooperate":
        print(player_score(3, 3))

    if play1 == "Cooperate" and play2 == "Defect":
        print(player_score(0, 5))

    if play1 == "Defect" and play2 == "Cooperate":
        print(player_score(5, 0))

    if play1 == "Defect" and play2 == "Defect":
        print(player_score(1, 1))

    current_round += 1

print(player_1_score, player_2_score)

with open("score_log.txt", "a") as log:
    players_choices = zip(player_1_choice, player_2_choice)

    for player1, player2 in players_choices:
        log.write("\n")
        log.write(f"(Player1: {player1})  ")
        log.write(f"(Player2: {player2})\n")
    log.write("***** \n")
    log.write(str(f"Score do player 1 = {player_1_score}\n"))
    log.write(str(f"Score do player 2 = {player_2_score}\n"))
