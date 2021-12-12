#!/usr/bin/env python
#Filename: Day09-02.py

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
|         Day 09 - Riddle 02         |
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
low_point_coordinates = []
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
            low_point_coordinates.append([row_count, col_count])

# Get the basin sizes
basin_sizes = []
for curr_low_point in low_point_coordinates:
    points_in_basin = [[curr_low_point[0], curr_low_point[1]]]

    for curr_point in points_in_basin:
        row, col = curr_point[0], curr_point[1]

        neighbor_points = [
            [row + 1, col],
            [row, col + 1],
            [row - 1, col],
            [row, col - 1]
        ]

        for neighbor_point in neighbor_points:
            if neighbor_point not in points_in_basin and bounded_height_map[neighbor_point[0]][neighbor_point[1]] != 9:
                points_in_basin.append(neighbor_point)

    basin_sizes.append(len(points_in_basin))

basin_sizes.sort()    

product = 1
for item in basin_sizes[-3:]:
    product *= item

# Print the result
print("The product of the sizes of the largest three bins is given by {}.".format(product))
