#!/usr/bin/env python
#Filename: Day07-01.py

 ###############################################################################################################
#                                                                                                               #
#                               Advent of Code 2021 - Solutions of Problems                                     #
#                                                                                                               #
#   Author:     Marcel Krause                                                                                   #
#   Date:       07.12.2021                                                                                      #
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
|         Day 07 - Riddle 01         |
|                                    |
+------------------------------------+
''')

# Read the input file
with open('Day07-01_input.dat', 'r') as content_file:
    all_lines = [line.rstrip('\n') for line in content_file]
    crab_positions = list(map(lambda x: int(x), all_lines[0].split(',')))
    min_val, max_val = min(crab_positions), max(crab_positions)

# Get the minimum amount of fuel
min_fuel = float('Inf')
for i in range(min_val, max_val+1):
    fuel = 0
    for j in crab_positions:
        fuel += abs(i-j)
    if fuel < min_fuel:
        min_fuel = fuel

# Print the result
print("The crabs must spent {} units of fuel to align with the least amount of fuel.".format(min_fuel))
