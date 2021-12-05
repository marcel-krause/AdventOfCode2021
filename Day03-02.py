#!/usr/bin/env python
#Filename: Day03-02.py

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

# Filter the bits with the given criterium
def bit_criteria_filter(bit_list: list, filter_criterium: int) -> int:
    filter_list = bit_list
    j = 0
    while True:
        counter = [0 for _ in range(len(filter_list[0]))]
        for curr in filter_list:
            for i in range(len(curr)):
                counter[i] += int(curr[i])

        filter_criterium_list = list(map(lambda x: '0' if x < len(filter_list)/2 else '1', counter)) if filter_criterium == 0 else list(map(lambda x: '1' if x < len(filter_list)/2 else '0', counter))

        filter_list = [line for line in filter_list if line[j] == filter_criterium_list[j]]
        if len(filter_list) == 1:
            target_binary = ''.join(filter_list)
            return int(target_binary, 2)

        j += 1

# Print the welcome screen
print('''
+------------------------------------+
|                                    |
|           Advent of Code           |
|         Day 03 - Riddle 02         |
|                                    |
+------------------------------------+
''')

# Read the input file
with open('Day03-01_input.dat', 'r') as content_file:
    all_lines = [line.rstrip('\n') for line in content_file]

# Calculate the oxygen and CO2 ratings
oxygen_rating = bit_criteria_filter(all_lines, 0)
co2_rating = bit_criteria_filter(all_lines, 1)

# Calculate the life support rating
life_support_rating = oxygen_rating * co2_rating

# Print the result
print("The life support rating of the submarine is given by {}.".format(life_support_rating))