#!/usr/bin/env python
#Filename: Day06-02.py

 ###############################################################################################################
#                                                                                                               #
#                               Advent of Code 2021 - Solutions of Problems                                     #
#                                                                                                               #
#   Author:     Marcel Krause                                                                                   #
#   Date:       06.12.2021                                                                                      #
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
|         Day 06 - Riddle 02         |
|                                    |
+------------------------------------+
''')

# Read the input file
with open('Day06-01_input.dat', 'r') as content_file:
    all_lines = [line.rstrip('\n') for line in content_file]
    all_starting_times = list(map(lambda x: int(x), all_lines[0].split(',')))

# Set initial configuration of lanternfish
all_lanternfish = {day: 0 for day in range(9)}
for starting_time in all_starting_times:
    all_lanternfish[starting_time] += 1

# Iterate over all days and generate new fish, if necessary
target_days = 256
for day in range(1, target_days+1):
    newly_created_fish = all_lanternfish[0]
    for timer, count in all_lanternfish.items():
        if timer < 8:
            all_lanternfish[timer] = all_lanternfish[timer+1]
    all_lanternfish[6] += newly_created_fish
    all_lanternfish[8] = newly_created_fish

# Count all lanternfish
fish_counter = sum(all_lanternfish.values())

# Print the result
print("There are {} lanternfish after {} days.".format(fish_counter, target_days))
