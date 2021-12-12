#!/usr/bin/env python
#Filename: Day08-02.py

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
|         Day 08 - Riddle 02         |
|                                    |
+------------------------------------+
''')

# Read the input file
with open('Day08-01_input.dat', 'r') as content_file:
    all_lines = [line.rstrip('\n') for line in content_file]

# Get the configuration of each segment and calculate the sum of all digits
# The reference configuration for each segment is as following:
#   aaaa
#  b    c
#  b    c
#   dddd
#  e    f
#  e    f
#   gggg
sum_of_all_digits = 0
all_chars = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
digit_configuration = {
    'abcefg': '0',
    'cf': '1',
    'acdeg': '2',
    'acdfg': '3',
    'bcdf': '4',
    'abdfg': '5',
    'abdefg': '6',
    'acf': '7',
    'abcdefg': '8',
    'abcdfg': '9'
}
for line in all_lines:
    initialization_line = line.split(' | ')[0]
    configurations = initialization_line.split()
    output = line.split(' | ')[1].split()

    # Find out which segment corresponds to 'a'
    segment_configuration = {}
    for initialization_sequence in configurations:
        if len(initialization_sequence) == 2:
            digit_1 = {i for i in initialization_sequence}
        elif len(initialization_sequence) == 3:
            digit_7 = {i for i in initialization_sequence}
        elif len(initialization_sequence) == 4:
            digit_4 = {i for i in initialization_sequence}
    segment_configuration[next(iter(digit_7 - digit_1))] = 'a'
    
    # Find out all other segments apart from 'd' and 'g'
    for char in all_chars:
        char_count = initialization_line.count(char)
        if char_count == 4:
            segment_configuration[char] = 'e'
        elif char_count == 6:
            segment_configuration[char] = 'b'
        elif char_count == 8:
            if char not in segment_configuration.keys():
                segment_configuration[char] = 'c'
        elif char_count == 9:
            segment_configuration[char] = 'f'

    # Find out the configuration for 'd' and 'g'
    segment_configuration[next(iter({i for i in digit_4 if i not in segment_configuration.keys()}))] = 'd'
    segment_configuration[next(iter(all_chars - set(segment_configuration.keys())))] = 'g'

    # Replace the output digit configuration with the original one and get the actual digits
    output_replaced = [''.join(sorted(list(map(lambda x: segment_configuration[x], output_number)))) for output_number in output]
    output_digit = int(''.join([digit_configuration[x] for x in output_replaced]))
    sum_of_all_digits += output_digit

# Print the result
print("The sum of all output values is given by {}.".format(sum_of_all_digits))
