#!/usr/bin/env python
#Filename: Day05-01.py

 ###############################################################################################################
#                                                                                                               #
#                               Advent of Code 2021 - Solutions of Problems                                     #
#                                                                                                               #
#   Author:     Marcel Krause                                                                                   #
#   Date:       05.12.2021                                                                                      #
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
|         Day 05 - Riddle 01         |
|                                    |
+------------------------------------+
''')

# Read the input file and get the coordinates
all_coords = []
max_coord = 0
with open('Day05-01_input.dat', 'r') as content_file:
    # all_lines = [line.rstrip('\n') for line in content_file]
    for line in content_file:
        coord_pair = line.rstrip('\n').split(' -> ')
        x1, y1 = list(map(lambda x: int(x), coord_pair[0].split(',')))
        x2, y2 = list(map(lambda x: int(x), coord_pair[1].split(',')))
        all_coords.append({'x1': x1, 'x2': x2, 'y1': y1, 'y2': y2})

        pot_max = max([x1, x2, y1, y2]) + 1
        if pot_max > max_coord:
            max_coord = pot_max

# Generate the empty grid
grid = [ [0 for _ in range(max_coord)] for _ in range(max_coord) ]

# Put all horizontal and vertical vents into the grid
for curr_coord in all_coords:
    x1, x2, y1, y2 = curr_coord['x1'], curr_coord['x2'], curr_coord['y1'], curr_coord['y2']

    if x1 == x2:
        y_min, y_max = min(y1, y2), max(y1, y2)

        for y in range(y_min, y_max+1):
            grid[y][x1] += 1
    elif y1 == y2:
        x_min, x_max = min(x1, x2), max(x1, x2)
        
        for x in range(x_min, x_max+1):
            grid[y1][x] += 1

# Count the number of overlapping vent lines
num_overlapping_vents = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] > 1:
            num_overlapping_vents += 1

# Print the result
print("At {} points at least two lines overlap.".format(num_overlapping_vents))
