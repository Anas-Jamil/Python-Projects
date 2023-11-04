# GOBLIN BATTLE
# Simulates a battle system between a player and goblins.
# Much can be added or improved here -- have at it!
import random

# View a player's stats.
def view_stats(player):
    print("Your stats are: ")
    print("Name:", player[0])
    print("Strength:", player[1])
    print("Agility:", player[2])
    print("Luck:", player[3])
    print("HP:", player[4])
    print("Kills:", player[5])

# Load the player stats from a file, if it exists.
def get_stats():
    try:
        player_file = open("player_stats.txt", "r")
    except FileNotFoundError:
        print("No player stats found. Create a character first.")
        return []
    else:
        player = [] # name, str, agi, luc, hp, kills
        player.append(player_file.readline().strip())
        for line in player_file:
            player.append(int(line))
        player_file.close()
        print("Player successfully loaded.")
        view_stats(player)
        return player

# Save the player stats to a file.
def save_stats(player):
    if len(player) == 0:
        print("No character to save.")
    else:
        try:
            player_file = open("player_stats.txt", "w")
        except OSError:
            print("Something is preventing the file from being written.")
        else:
            for val in player:
                player_file.write(str(val)+"\n")
            player_file.close()
            print("Stats successfully written.")

# Create a player with randomized stats.
def make_player():
    player = []
    name = input("What is your name, brave warrior? ")
    player.append(name.strip()) # name
    for i in range(3):
        player.append(random.randint(1, 6) + 6) # str, agi and luck
    player.append(30) # HP
    player.append(0) # kills
    view_stats(player)
    return player

# Create a goblin with randomized stats.
def make_goblin():
    goblin_types = ("forest", "mountain", "cave")
    goblin = [random.choice(goblin_types)]
    for i in range(3):
        goblin.append(5 + random.randint(1, 6))
    goblin.append(random.randint(8, 14))
    return goblin

# Display tha main menu.
def menu():
    print("1. Create new character.")
    print("2. Load existing character.")
    print("3. View stats.")
    print("4. Hunt some goblins.")
    print("5. Save progress and quit.")
    action = input("What would you like to do? ")
    while action not in ["1", "2", "3", "4", "5"]:
        action = input("Please enter a value 1-5: ")
    return action

# Calculate the damage, based on an attacker's strength and luck.
def calc_damage(winner, loser):
    winner_force = winner[1] + random.randint(1, 10)
    loser_force = loser[1] + random.randint(1, 10)
    if winner_force > loser_force:
        damage = 3
    elif winner_force == loser_force:
        damage = 2
    else:
        damage = 1
    if winner[3] + random.randint(1, 10) > 15:
        damage += 1
    return damage

# Fight a battle to the death between the player and a goblin.
def battle(player):
    if len(player) == 0 or player[4] <= 0:
        print("You must first create a new character.")
        return player
    else:
        goblin = make_goblin()
        print("You scour the countryside and encounter a {} goblin.".format(goblin[0]))
        while player[4] > 0 and goblin[4] > 0:
            print("You have {} HP, and the goblin has {} HP.".format(player[4], goblin[4]))
            player_attack = player[2] + random.randint(1, 10)
            goblin_attack = goblin[2] + random.randint(1, 10)
            if player_attack > goblin_attack:
                damage = calc_damage(player, goblin)
                print("You hit the goblin for {} points of damage.".format(damage))
                goblin[4] -= damage
            elif player_attack < goblin_attack:
                damage = calc_damage(goblin, player)
                print("The goblin hit you for {} points of damage.".format(damage))
                player[4] -= damage
            else:
                print("You and the goblin miss each other.")
        if player[4] < 0:
            print("You have been slain by the {} goblin.".format(goblin[0]))
            player[4] = 0
        else:
            print("You have slain the {} goblin, brave {}.".format(goblin[0], player[0]))
            player[5] += 1
        return player

# MAIN PROGRAM
player = []
while True:
    action = menu()
    if action == "1":
        player = make_player()
    elif action == "2":
        player = get_stats()
    elif action == "3":
        view_stats(player)
    elif action == "4":
        player = battle(player)
    else:
        save_stats(player)
        break
print("Thank you for playing.")