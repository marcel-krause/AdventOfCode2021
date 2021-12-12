#!/usr/bin/env python
#Filename: Day09-01.py

 ###############################################################################################################
#                                                                                                               #
#                               Advent of Code 2021 - Solutions of Problems                                     #
#                                                                                                               #
#   Author:     Marcel Krause                                                                                   #
#   Date:       09.12.2021                                                                                      #
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
|         Day 09 - Riddle 01         |
|                                    |
+------------------------------------+
''')

# Read the input file
with open('Day09-01_input.dat', 'r') as content_file:
    all_lines = [line.rstrip('\n') for line in content_file]

# Get the height map from the input
height_map = []
for line in all_lines:
    row = [int(x) for x in line]
    height_map.append(row)

# Put a border around the map
bounded_height_map = [[9]*(len(height_map[0])+2)]
for row in height_map:
    bounded_height_map.append([9] + row + [9])
bounded_height_map.append([9]*(len(height_map[0])+2))

# Find the local minima
low_points = []
for row_count in range(1, len(bounded_height_map) - 1):
    for col_count in range(1, len(bounded_height_map[0]) - 1):
        curr_point = bounded_height_map[row_count][col_count]

        neighbor_points = [
            bounded_height_map[row_count-1][col_count],
            bounded_height_map[row_count][col_count+1],
            bounded_height_map[row_count+1][col_count],
            bounded_height_map[row_count][col_count-1]
        ]

        if all(curr_point < i for i in neighbor_points):
            low_points.append(curr_point)

# Calculate the risk level
risk_levels = [x + 1 for x in low_points]
sum_of_risk_levels =sum(risk_levels)

# Print the result
print("{}".format(sum_of_risk_levels))
