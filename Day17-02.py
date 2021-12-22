#!/usr/bin/env python
#Filename: Day17-02.py

 ###############################################################################################################
#                                                                                                               #
#                               Advent of Code 2021 - Solutions of Problems                                     #
#                                                                                                               #
#   Author:     Marcel Krause                                                                                   #
#   Date:       17.12.2021                                                                                      #
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
|         Day 17 - Riddle 02         |
|                                    |
+------------------------------------+
''')

# Import modules
from math import sqrt, ceil

# Read the input file
with open('Day17-01_input.dat', 'r') as content_file:
    all_lines = [line.rstrip('\n') for line in content_file]

# Get the target areas
area_ranges = all_lines[0].replace("target area: ", "").split(", ")
x_ranges = area_ranges[0].replace("x=", "").split("..")
y_ranges = area_ranges[1].replace("y=", "").split("..")
x_range_target_area = set(range(int(x_ranges[0]), int(x_ranges[1]) + 1))
y_range_target_area = set(range(int(y_ranges[0]), int(y_ranges[1]) + 1))
max_x_in_target = max(x_range_target_area)
min_y_in_target = min(y_range_target_area)

# Find all valid trajectories
largest_y_reached = -float("Inf")
valid_configurations = set()
x_range_min = ceil((sqrt(1 + 8*int(x_ranges[0])) - 1)/2)
for x in range(x_range_min, int(x_ranges[1])+1):
    for y in range(int(y_ranges[0]), -int(y_ranges[0])):

        # Initialize the probe
        probe_position = [0, 0]
        probe_velocity = [x, y]
        max_y_position = -float("Inf")

        # Perform the steps
        for step in range(1000):
            # Probe movement
            probe_position[0] += probe_velocity[0]
            probe_position[1] += probe_velocity[1]

            # Update the largest y value, if necessary
            if probe_position[1] > max_y_position:
                max_y_position = probe_position[1]

            # Drag influence
            if probe_velocity[0] > 0:
                probe_velocity[0] -= 1
            elif probe_velocity[0] < 0:
                probe_velocity[0] += 1
            
            # Gravity influence
            probe_velocity[1] -= 1

            # Check if the probe has entered the target area
            if probe_position[0] in x_range_target_area and probe_position[1] in y_range_target_area:
                valid_configurations.add((x, y))
                if max_y_position > largest_y_reached:
                    largest_y_reached = max_y_position
                break
            
            # Check if the probe overshoots
            if probe_position[0] > max_x_in_target or probe_position[1] < min_y_in_target:
                break

valid_configurations_count = len(valid_configurations)

# Print the result
print("{} initial velocities will send the probe to the targert area.".format(valid_configurations_count))
