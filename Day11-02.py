#!/usr/bin/env python
#Filename: Day11-02.py

 ###############################################################################################################
#                                                                                                               #
#                               Advent of Code 2021 - Solutions of Problems                                     #
#                                                                                                               #
#   Author:     Marcel Krause                                                                                   #
#   Date:       11.12.2021                                                                                      #
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
|         Day 11 - Riddle 02         |
|                                    |
+------------------------------------+
''')

# Read the input file
energy_levels = []
with open('Day11-01_input.dat', 'r') as content_file:
    for line in content_file:
        temp_line = []
        for char in line.rstrip('\n'):
            temp_line.append(int(char))
        energy_levels.append(temp_line)

# Put a border around the map
bounded_energy_levels = [[float("-Inf")]*(len(energy_levels[0])+2)]
for row in energy_levels:
    bounded_energy_levels.append([float("-Inf")] + row + [float("-Inf")])
bounded_energy_levels.append([float("-Inf")]*(len(energy_levels[0])+2))
energy_levels = bounded_energy_levels

# Perform the steps
step = 1
while True:
    # Increase the energy count of the current octopus and get the locations of all initially flashing octopuses
    flashing_octopuses = []
    for row in range(len(energy_levels)):
        for col in range(len(energy_levels[0])):
            energy_levels[row][col] += 1
            if energy_levels[row][col] == 10:
                flashing_octopuses.append([row, col])

    # Flash the octopuses and increase the energy levels of the neighbors
    for row, col in flashing_octopuses:
        for neighbor_row in range(row-1, row+2):
            for neighbor_col in range(col-1, col+2):
                if neighbor_row == row and neighbor_col == col:
                    continue
                energy_levels[neighbor_row][neighbor_col] += 1
                if energy_levels[neighbor_row][neighbor_col] == 10 and [neighbor_row, neighbor_col] not in flashing_octopuses:
                    flashing_octopuses.append([neighbor_row, neighbor_col])

    # Check if all octopuses flashed at the same time
    if all(all(j > 9 or j == float("-inf") for j in i) for i in energy_levels):
        break

    # Reset all octopuses that flashed
    for row in range(len(energy_levels)):
        for col in range(len(energy_levels[0])):
            if energy_levels[row][col] > 9:
                energy_levels[row][col] = 0

    step += 1

# Print the result
print("During step {}, all octopuses flash simultaneously.".format(step))
