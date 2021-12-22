#!/usr/bin/env python
#Filename: Day21-02.py

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
|         Day 21 - Riddle 02         |
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
game_states = { (player_1_points, player_1_position, player_2_points, player_2_position): 1 }

# Count the total number of wins for each player
wins_for_player_1 = 0
wins_for_player_2 = 0

# Get all possible sums of three consecutive three-sided dice rolls and their multiplicity
possible_dice_rolls = [ d1 + d2 + d3 for d1 in range(1,4) for d2 in range(1, 4) for d3 in range(1, 4) ]
dice_outcomes = {}
for i in possible_dice_rolls:
    if i not in dice_outcomes:
        dice_outcomes[i] = 1
    else:
        dice_outcomes[i] += 1

# Play all games in all universes until there are no open games left
points_for_win = 21
while len(game_states) > 0:

    # Iterate over all current game states
    new_game_states = {}
    for game_state, game_state_multiplicity in game_states.items():
        
        # Player 1 rolls the dice
        for dice_roll_1, multiplicity_1 in dice_outcomes.items():
            # Update the position of player 1
            player_1_position = (game_state[1] + dice_roll_1 - 1)%10 + 1

            # Update the points of player 1
            player_1_points = game_state[0] + player_1_position

            # End this game state in case of a win
            if player_1_points >= points_for_win:
                wins_for_player_1 += multiplicity_1*game_state_multiplicity
                continue
            
            # Player 2 rolls the dice
            for dice_roll_2, multiplicity_2 in dice_outcomes.items():
                # Update the position of player 2
                player_2_position = (game_state[3] + dice_roll_2 - 1)%10 + 1
                
                # Update the points of player 2
                player_2_points = game_state[2] + player_2_position

                # End this game state in case of a win
                if player_2_points >= points_for_win:
                    wins_for_player_2 += multiplicity_1*multiplicity_2*game_state_multiplicity
                    continue
                
                # In case no player wins, add the new game state to the set of open game states
                curr_game_state = (player_1_points, player_1_position, player_2_points, player_2_position)
                if curr_game_state in new_game_states:
                    new_game_states[curr_game_state] += multiplicity_1*multiplicity_2*game_state_multiplicity
                else:
                    new_game_states[curr_game_state] = multiplicity_1*multiplicity_2*game_state_multiplicity

    game_states = new_game_states.copy()

# Determine the winner
if wins_for_player_1 > wins_for_player_2:
    winning_player = 1
    max_result = wins_for_player_1
else:
    winning_player = 2
    max_result = wins_for_player_2

# Print the result
print("Player {} wins more than the other player, in total in {} universes.".format(winning_player, max_result))
