#!/usr/bin/env python
#Filename: Day22-01.py

 ###############################################################################################################
#                                                                                                               #
#                               Advent of Code 2021 - Solutions of Problems                                     #
#                                                                                                               #
#   Author:     Marcel Krause                                                                                   #
#   Date:       22.12.2021                                                                                      #
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
|         Day 22 - Riddle 01         |
|                                    |
+------------------------------------+
''')

# Read the input file
with open('Day22-01_input.dat', 'r') as content_file:
    all_lines = [line.rstrip('\n') for line in content_file]

# Create a list of all instructions from the input file
instructions = []
for line in all_lines:
    turn_state = int("on" in line)

    x, y, z = line.replace("on ", "").replace("off ", "").split(",")

    x = list(map(lambda x: int(x), x.replace("x=", "").split("..")))
    y = list(map(lambda x: int(x), y.replace("y=", "").split("..")))
    z = list(map(lambda x: int(x), z.replace("z=", "").split("..")))

    instructions.append((x, y, z, turn_state))

# Iterate over all instructions
grid = {}
for instruction in instructions:
    # Get the current cube and its on/off state
    x_range = range(instruction[0][0], instruction[0][1]+1)
    y_range = range(instruction[1][0], instruction[1][1]+1)
    z_range = range(instruction[2][0], instruction[2][1]+1)
    state = instruction[3]

    # Only consider the initialization region
    if max(x_range) < -50 or min(x_range) > 50 or max(y_range) < -50 or min(y_range) > 50 or max(z_range) < -50 or min(z_range) > 50:
        continue

    # Switch the lights on or off
    for x in x_range:
        for y in y_range:
            for z in z_range:
                key = str(x) + "," + str(y) + "," + str(z)
                grid[key] = state

# Count all lights that are turned on
lights_turned_on = 0
for i in grid.values():
    lights_turned_on += int(i)

# Print the result
print("After performing all steps in the initialization region, there are {} lights turned on.".format(lights_turned_on))
