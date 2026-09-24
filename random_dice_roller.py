import random


def roll_dice(number_of_dice):
    results = []

    for _ in range(number_of_dice):
        results.append(random.randint(1, 6))

    return results


def display_results(results):
    print("\nDice Results:")

    for i, value in enumerate(results, start=1):
        print(f"Dice {i}: {value}")

    print(f"\nTotal = {sum(results)}")


def main():
    print("===== RANDOM DICE ROLLER =====")

    while True:
        try:
            number_of_dice = int(input("\nEnter number of dice (0 to exit): "))

            if number_of_dice == 0:
                print("Thanks for using the Dice Roller!")
                break

            if number_of_dice < 0:
                print("Please enter a positive number.")
                continue

            results = roll_dice(number_of_dice)
            display_results(results)

        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()
