#!/usr/bin/env python
#Filename: Day02-01.py

 ###############################################################################################################
#                                                                                                               #
#                               Advent of Code 2021 - Solutions of Problems                                     #
#                                                                                                               #
#   Author:     Marcel Krause                                                                                   #
#   Date:       02.12.2021                                                                                      #
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
|         Day 02 - Riddle 01         |
|                                    |
+------------------------------------+
''')

# Read the input file
with open('Day02-01_input.dat', 'r') as content_file:
    all_lines = [line.rstrip('\n') for line in content_file]

# Find the final positions of the submarine
horizontal_position = 0
depth = 0
for line in all_lines:
    curr_pos_change = int(line.split()[1])
    
    if 'forward' in line:
        horizontal_position += curr_pos_change
    if 'down' in line:
        depth += curr_pos_change
    if 'up' in line:
        depth -= curr_pos_change

# Print the result
print("The product of the final horizontal position and depth is given by {}.".format(horizontal_position*depth))
