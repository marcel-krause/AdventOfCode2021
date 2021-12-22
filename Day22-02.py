#!/usr/bin/env python
#Filename: Day22-02.py

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
|         Day 22 - Riddle 02         |
|                                    |
+------------------------------------+
''')


def get_intersect_of_two_cubes(cube_1: tuple[tuple[int]], cube_2: tuple[tuple[int]]) -> tuple:
    # Find the minimum "right-most" x borders and the maximum "left-most" x borders (note: the ternary operator is actually faster compared to min() and max())
    x_min = cube_1[0][1] if cube_1[0][1] < cube_2[0][1] else cube_2[0][1]
    x_max = cube_1[0][0] if cube_1[0][0] > cube_2[0][0] else cube_2[0][0]

    # Find the minimum "right-most" y borders and the maximum "left-most" y borders
    y_min = cube_1[1][1] if cube_1[1][1] < cube_2[1][1] else cube_2[1][1]
    y_max = cube_1[1][0] if cube_1[1][0] > cube_2[1][0] else cube_2[1][0]

    # Find the minimum "right-most" z borders and the maximum "left-most" z borders
    z_min = cube_1[2][1] if cube_1[2][1] < cube_2[2][1] else cube_2[2][1]
    z_max = cube_1[2][0] if cube_1[2][0] > cube_2[2][0] else cube_2[2][0]

    # In case no overlap is found, return false
    if x_min < x_max or y_min < y_max or z_min < z_max:
        return ()
    
    # Return the cube representing the overlap
    return ( (x_max, x_min), (y_max, y_min), (z_max, z_min) )


def get_cube_volume(cube: tuple[tuple[int]]) -> int:
    return (cube[0][1] - cube[0][0] + 1)*(cube[1][1] - cube[1][0] + 1)*(cube[2][1] - cube[2][0] + 1)


# Read the input file
with open('Day22-01_input.dat', 'r') as content_file:
    all_lines = [line.rstrip('\n') for line in content_file]

# Create a list of all instructions from the input file
instructions = []
for line in all_lines:
    turn_state = int("on" in line)

    x, y, z = line.replace("on ", "").replace("off ", "").split(",")
    x = tuple(map(lambda x: int(x), x.replace("x=", "").split("..")))
    y = tuple(map(lambda x: int(x), y.replace("y=", "").split("..")))
    z = tuple(map(lambda x: int(x), z.replace("z=", "").split("..")))

    instructions.append(((x, y, z), turn_state))

# Initialize a list of all signed volumes and a dictionary previously considered cubes, including newly created intersects
signed_volumes = []
cubes = {}

# Iterate over all instructions
for curr_instruction in instructions:

    # For each instruction, iterate over previous cubes (including intersects)
    add_cubes = cubes.copy()
    for cube in cubes.items():
        # Check for intersects of the current new cube and the current previously considered cube/intersect
        intersect = get_intersect_of_two_cubes(cube[0], curr_instruction[0])
        
        # If no intersect is found, continue with the next previously considered cube
        if len(intersect) == 0:
            continue
        
        # Add the intersect to the dict of previously considered cubes and add the volume with the correct sign
        if cube[1] != 0:
            signed_volumes.append(-1*cube[1]*get_cube_volume(intersect))
        if intersect in add_cubes:
            add_cubes[intersect] += -1*cube[1]
        else:
            add_cubes[intersect] = -1*cube[1]

    # In case the current new cube is of type "on", add it to the dict of previously considered cubes or update the value if it is already present
    if curr_instruction[1] == 1:
        if curr_instruction[1] != 0:
            signed_volumes.append(curr_instruction[1]*get_cube_volume(curr_instruction[0]))
        if curr_instruction[0] in add_cubes:
            add_cubes[curr_instruction[0]] += 1*curr_instruction[1]
        else:
            add_cubes[curr_instruction[0]] = 1*curr_instruction[1]

    # Update the dict with all previously considered cubes
    cubes = add_cubes.copy()

# Get the result
lights_turned_on = sum(signed_volumes)

# Print the result
print("After executing all steps, there are {} lights turned on.".format(lights_turned_on))
