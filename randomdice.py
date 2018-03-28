#!/bin/python3

import random

Input = False
while not Input:
    try:
        dice = int(input("How many sides does the dice have? "))
        rolls = int(input("How many rolls? "))
        Input = True
    except ValueError:
        Input = False
exit = False
while not exit:
    numbers = []
    for x in range(0, rolls):
        numbers.append(random.randint(1,dice))
    print(numbers)
    if input("Reroll? (y/n)") == "n":
        exit = True