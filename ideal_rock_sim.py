import generate_bags
import random

def print_final_results(wins):
    print("\nFinal Simulation Results")
    print("Player 1 Win Total:", wins[1])
    print("Player 2 Win Total:", wins[2])
    print("Player 3 Win Total:", wins[3])

def ideal_rock_sim(sims):
    bags = generate_bags.generate_bags(sims)

    wins = {1: 0, 2: 0, 3: 0}
    
    for bag in bags:
        # Player 1 Turn
        rock = random.randint(0, 2)
        player_1 = bag.pop(rock)
        if player_1 == 1:
            print("Player 1 wins")
            wins[1] += 1
            continue

        # Player 2 Turn
        rock = random.randint(0, 1)
        player_2 = bag.pop(rock)

        # Player 3 Turn
        player_3 = player_2

        # Player 2 takes rock from bag after steal
        player_2 = bag[0]

        if player_2 == 1:
            print("Player 2 wins")
            wins[2] += 1
        else:
            print("Player 3 wins")
            wins[3] += 1
    
    print_final_results(wins)



ideal_rock_sim(10000000)