import random

def generate_bags(sims):
    print("Generating", sims, "bags for survivor rock game simulation")

    bags = []

    for i in range(sims):
        current_bag = [0, 0, 0]
        purple_rock = random.randint(0, 2)
        current_bag[purple_rock] = 1
        bags.append(current_bag[:])
    
    return bags
