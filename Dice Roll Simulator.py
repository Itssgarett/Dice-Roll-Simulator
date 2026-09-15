import random
import time

print("It is currently " + time.strftime("%Y-%m-%d %H:%M:%S"))
print("Welcome to the Dice Roll Simulator!")

def roll_dice(num_rolls):
    results = []
    for _ in range(num_rolls):
        roll = random.randint(1, 6)
        results.append(roll)
    return results

def player(player_number):
    player_name = input(f"Enter Player{player_number}'s Name: ")
    print(f"Hello, {player_name}! You are Player{player_number}. Goodluck!")
    return player_name

def game():
    player1_name = player(1)
    player2_name = player(2)

    num_rolls = int(input("How many times would you like to roll the dice? "))

    player1_rolls = roll_dice(num_rolls)
    player2_rolls = roll_dice(num_rolls)

    print(f"\n{player1_name}'s rolls: {player1_rolls}")
    print(f"(Total: {sum(player1_rolls)})")

    print(f"\n{player2_name}'s rolls: {player2_rolls}")
    print(f"(Total: {sum(player2_rolls)})")

    if sum(player1_rolls) > sum(player2_rolls):
        print(f"\n{player1_name} wins!")
    elif sum(player1_rolls) < sum(player2_rolls):
        print(f"\n{player2_name} wins!")
    else:
        print("\n It's a tie!")

if __name__ == "__main__":
    game()



 
   