import random

def roll_dice(num_dice):
    results = []
    for _ in range(num_dice):
        roll_result = random.randint(1, 6)  # Simulate a roll of a six-sided die
        results.append(roll_result)
    return results

def main():
    print("Dice Rolling Simulator")
    while True:
        try:
            num_dice = int(input("How many dice would you like to roll? "))
            if num_dice <= 0:
                print("Please enter a positive number of dice.")
                continue

            dice_results = roll_dice(num_dice)
            print(f"Results: {dice_results}")
        except ValueError:
            print("Invalid input. Please enter a valid number of dice.")
        
        play_again = input("Roll again? (yes/no): ").lower()
        if play_again != "yes":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
