#!/usr/bin/env python
#Filename: Day21-01.py

 ###############################################################################################################
#                                                                                                               #
#                               Advent of Code 2021 - Solutions of Problems                                     #
#                                                                                                               #
#   Author:     Marcel Krause                                                                                   #
#   Date:       21.12.2021                                                                                      #
#   Copyright:  Copyright (C) 2021, Marcel Krause                                                               #
#   License:    GNU General Public License (GNU GPL-3.0-or-later)                                               #
#                                                                                                               #
#               This program is released under GNU General Public License (GNU GPL-3.0-or-later).               #
#               This program is free software: you can redistribute it and/or modify it under the terms of the  #
#               GNU General Public License as published by the Free Software Foundation, either version 3 of    #
#               the License, or any later version.                                                              #
#                                                                                                               #
#               This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;       #
#               without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.       #
#               See the GNU General Public License for more details.                                            #
#                                                                                                               #
#               You have received a copy LICENSE.md of the GNU General Public License along with this program.  #
#                                                                                                               #
 ###############################################################################################################


# Print the welcome screen
print('''
+------------------------------------+
|                                    |
|           Advent of Code           |
|         Day 21 - Riddle 01         |
|                                    |
+------------------------------------+
''')

# Read the input file
with open('Day21-01_input.dat', 'r') as content_file:
    all_lines = [line.rstrip('\n') for line in content_file]

# Get the players' starting positions
player_1_position = int(all_lines[0].split()[-1])
player_2_position = int(all_lines[1].split()[-1])

# Initialize the starting game state
player_1_points = 0
player_2_points = 0
previous_dice_roll = 0

# Play the game until the first player reaches the points to win the game
dice_rolls = 0
points_for_win = 1000
while True:
    # Roll the dices for player 1
    dice_roll = 0
    for _ in range(3):
        previous_dice_roll += 1
        dice_roll += previous_dice_roll
        dice_rolls += 1
    
    # Update the position of player 1
    player_1_position = (player_1_position + dice_roll - 1)%10 + 1

    # Update the points of player 1 and end this game state in case of a win
    player_1_points += player_1_position
    if player_1_points >= points_for_win:
        break

    # Roll the dices for player 2
    dice_roll = 0
    for _ in range(3):
        previous_dice_roll += 1
        dice_roll += previous_dice_roll
        dice_rolls += 1

    # Update the position of player 2
    player_2_position = (player_2_position + dice_roll - 1)%10 + 1

    # Update the points of player 2 and end this game state in case of a win
    player_2_points += player_2_position
    if player_2_points >= points_for_win:
        break

# Determine the result
if player_1_points > player_2_points:
    result = player_2_points*dice_rolls
else:
    result = player_1_points*dice_rolls

# Print the result
print("The product of the losing player's score and the amount the dice were rolled is {}.".format(result))
