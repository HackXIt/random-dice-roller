#!/bin/python3
# https://www.reddit.com/r/beginnerprojects/comments/1j50e7/project_dice_rolling_simulator/
import random

Input = False
while not Input:
    try:
        dice = int(input("How many sides does the dice have? "))
        rolls = int(input("How many rolls? "))
        Input = True
    except ValueError:
        Input = False 
collection = list()
exit = False
rolled = 0
while not exit:
    numbers = []
    for x in range(0, rolls):
        numbers.append(random.randint(1,dice))
    collection.append(numbers)
    print(numbers)
    if input("Reroll? (y/n)") == "n":
        exit = True
    else:
        exit = False
        rolled += 1
print(collection)