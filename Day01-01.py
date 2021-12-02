#!/usr/bin/env python
#Filename: Day01-01.py

 ###############################################################################################################
#                                                                                                               #
#                               Advent of Code 2021 - Solutions of Problems                                     #
#                                                                                                               #
#   Author:     Marcel Krause                                                                                   #
#   Date:       01.12.2021                                                                                      #
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


#----------------------------#
#        Main Program        #
#----------------------------#

if __name__ == "__main__":
    # Print the welcome screen
    print('''
+------------------------------------+
|                                    |
|           Advent of Code           |
|         Day 01 - Riddle 01         |
|                                    |
+------------------------------------+
    ''')

    # Read the input file
    with open('Day01-01_input.dat', 'r') as content_file:
        all_lines = [int(line.rstrip('\n')) for line in content_file]

    # Count the number of increases
    num_increases = 0
    for i in range(1, len(all_lines)):
        if all_lines[i] > all_lines[i-1]:
            num_increases += 1

    # Print the result
    print("{} measurements are larger than the previous one.".format(num_increases))
