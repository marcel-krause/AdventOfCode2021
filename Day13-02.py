#!/usr/bin/env python
#Filename: Day13-02.py

 ###############################################################################################################
#                                                                                                               #
#                               Advent of Code 2021 - Solutions of Problems                                     #
#                                                                                                               #
#   Author:     Marcel Krause                                                                                   #
#   Date:       13.12.2021                                                                                      #
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
|         Day 13 - Riddle 02         |
|                                    |
+------------------------------------+
''')

# Read the input file
with open('Day13-01_input.dat', 'r') as content_file:
    all_lines = [line.rstrip('\n') for line in content_file]

# Get all dot coordinates and the folding lines
dot_coordinates = []
folding_instructions = []
max_row = 0
max_col = 0
for line in all_lines:
    if ',' in line:
        col, row = list(map(lambda x: int(x), line.split(',')))
        dot_coordinates.append([row, col])
        if row > max_row:
            max_row = row
        if col > max_col:
            max_col = col
    if 'x=' in line:
        folding_instructions.append('x')
    if 'y=' in line:
        folding_instructions.append('y')

# Fill the initial dot grid
dot_grid = [ [0 for _ in range(max_col + 1)] for _ in range(max_row + 1) ]
for row, col in dot_coordinates:
    dot_grid[row][col] += 1

# Fold the paper according to the all instructions
for curr_folding_instruction in folding_instructions:
    if curr_folding_instruction == 'y':
        new_dot_grid = [ [0 for _ in range(len(dot_grid[0]))] for _ in range(len(dot_grid)//2) ]
        for row in range(len(dot_grid)//2):
            for col in range(len(dot_grid[0])):
                new_dot_grid[row][col] = dot_grid[row][col]

        dot_grid_copy = dot_grid.copy()
        dot_grid_copy.reverse()

        for row in range(len(dot_grid_copy)//2):
            for col in range(len(dot_grid_copy[0])):
                if dot_grid_copy[row][col] == 1:
                    new_dot_grid[row][col] = 1
    else:
        new_dot_grid = [ [0 for _ in range(len(dot_grid[0])//2)] for _ in range(len(dot_grid)) ]
        for row in range(len(dot_grid)):
            for col in range(len(dot_grid[0])//2):
                new_dot_grid[row][col] = dot_grid[row][col]

        dot_grid_copy = []
        for i in range(len(dot_grid)):
            curr_row = dot_grid[i].copy()
            curr_row.reverse()
            dot_grid_copy.append(curr_row)

        for row in range(len(dot_grid_copy)):
            for col in range(len(dot_grid_copy[0])//2):
                if dot_grid_copy[row][col] == 1:
                    new_dot_grid[row][col] = 1

    dot_grid = new_dot_grid.copy()

# Print the result
print("The code in the manual is given by:\n")
for row in new_dot_grid:
    print_row = ''
    for dot in row:
        if dot == 1:
            print_row += '*'
        else:
            print_row += ' '
    print(print_row)