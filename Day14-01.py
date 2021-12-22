#!/usr/bin/env python
#Filename: Day14-01.py

 ###############################################################################################################
#                                                                                                               #
#                               Advent of Code 2021 - Solutions of Problems                                     #
#                                                                                                               #
#   Author:     Marcel Krause                                                                                   #
#   Date:       14.12.2021                                                                                      #
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
|         Day 14 - Riddle 01         |
|                                    |
+------------------------------------+
''')

# Import required packages
import numpy as np

# Read the input file
with open('Day14-01_input.dat', 'r') as content_file:
    all_lines = [line.rstrip('\n') for line in content_file]

# Get the polymer template and all replacements
steps = 10
polymer_template = all_lines[0]
replacements = [all_lines[i] for i in range(2, len(all_lines))]

rep = {}
for i in replacements:
    key, val = i.split(' -> ')
    rep[key] = key[0] + val + key[1]
molecules = list(rep.keys())

# Construct the replacement matrix and exponentiate it
replacement_matrix_T = []
for key, val in rep.items():
    replacements = [val[:2], val[1:]]
    curr_row = [1 if i in replacements else 0 for i in molecules.copy()]
    replacement_matrix_T.append(curr_row)
replacement_matrix = np.array(replacement_matrix_T, dtype='int64').transpose()
replacement_matrix_exponentiated = np.linalg.matrix_power(replacement_matrix, steps)

# Convert the initial polymer to its final form
polymer_template_vector = np.array([1 if i in polymer_template else 0 for i in molecules], dtype='int64')
final_polymer_vector = replacement_matrix_exponentiated.dot(polymer_template_vector).tolist()

# Count the occurences of all elements
element_count = {polymer_template[0]: 1}
for i in range(len(final_polymer_vector)):
    if molecules[i][1] in element_count.keys():
        element_count[molecules[i][1]] += final_polymer_vector[i]
    else:
        element_count[molecules[i][1]] = final_polymer_vector[i]

# Get the difference between the quantities of the most and least common elements
difference_quantities = max(element_count.values()) - min(element_count.values())

# Print the result
print("The difference between the quantities of the most and least common elements in the final polymer after {} steps is {}.".format(steps, difference_quantities))
