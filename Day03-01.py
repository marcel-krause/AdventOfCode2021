#!/usr/bin/env python
#Filename: Day03-01.py

 ###############################################################################################################
#                                                                                                               #
#                               Advent of Code 2021 - Solutions of Problems                                     #
#                                                                                                               #
#   Author:     Marcel Krause                                                                                   #
#   Date:       03.12.2021                                                                                      #
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
|         Day 03 - Riddle 01         |
|                                    |
+------------------------------------+
''')

# Read the input file
with open('Day03-01_input.dat', 'r') as content_file:
    all_lines = [line.rstrip('\n') for line in content_file]

# Get the most and least common bits for each position
counter = [0 for _ in range(len(all_lines[0]))]
for curr in all_lines:
    for i in range(len(curr)):
        counter[i] += int(curr[i])
most_common_bits = ''.join(list(map(lambda x: '0' if x < len(all_lines)/2 else '1', counter)))
least_common_bits = ''.join(list(map(lambda x: '1' if x < len(all_lines)/2 else '0', counter)))

# Calculate the oxygen and CO2 ratings
gamma_rate = int(most_common_bits, 2)
epsilon_rate = int(least_common_bits, 2)

# Calculate the power consumption
power_consumption = gamma_rate * epsilon_rate

# Print the result
print("The power consumption of the submarine is given by {}.".format(power_consumption))
