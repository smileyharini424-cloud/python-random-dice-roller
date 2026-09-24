# Random Dice Roller

## Explanation

The Random Dice Roller is a Python program that simulates rolling dice. The user can choose how many dice to roll, and the program generates a random value from 1 to 6 for each die.

## Problem Statement

Create a Python program that allows the user to roll one or more six-sided dice and displays the result of each roll.

## Features

* Roll one or multiple dice
* Generates random values from 1 to 6
* Displays each dice result
* Calculates the total
* Allows repeated rolls
* Handles invalid input

## How It Works

1. The user enters the number of dice.
2. The program randomly generates a value from 1 to 6 for each die.
3. Each result is displayed.
4. The total of all dice is calculated.
5. The user can roll again or exit.

## Technologies Used

* Python
* `random` module
* Lists
* Loops
* Functions
* Exception Handling

## Data Structure Used

* List

## Methods Used

* `roll_dice()`
* `display_results()`
* `main()`

## Program Flow

```text
Start
  ↓
Enter Number of Dice
  ↓
Generate Random Values
  ↓
Store Results
  ↓
Display Results
  ↓
Calculate Total
  ↓
Roll Again / Exit
  ↓
End
```

## Sample Input

```text
Enter number of dice: 3
```

## Sample Output

```text
Dice 1: 4
Dice 2: 2
Dice 3: 6

Total = 12
```

## Time Complexity

O(n), where `n` is the number of dice.

## Space Complexity

O(n)

## Key Learning

* Using Python's `random` module
* Working with lists
* Using loops and functions
* Generating random values
* Handling user input

## File Location

`random_dice_roller.py`

## Repository Structure

```text
python-random-dice-roller/
│
├── random_dice_roller.py
└── README.md
```

## Author

V.Harini
