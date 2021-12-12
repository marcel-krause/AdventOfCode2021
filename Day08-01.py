#!/usr/bin/env python
#Filename: Day08-01.py

 ###############################################################################################################
#                                                                                                               #
#                               Advent of Code 2021 - Solutions of Problems                                     #
#                                                                                                               #
#   Author:     Marcel Krause                                                                                   #
#   Date:       08.12.2021                                                                                      #
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
|         Day 08 - Riddle 01         |
|                                    |
+------------------------------------+
''')

# Read the input file
with open('Day08-01_input.dat', 'r') as content_file:
    all_lines = [line.rstrip('\n') for line in content_file]

counter = 0
for line in all_lines:
    configurations = line.split(' | ')[0].split()
    output = line.split(' | ')[1].split()
    for out in output:
        if len(out) == 2 or len(out) == 4 or len(out) == 3 or len(out) == 7:
            counter += 1

# Print the result
print("The digits 1, 4, 7 or 8 appear {} times in the output values.".format(counter))
