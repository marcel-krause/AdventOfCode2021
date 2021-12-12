#!/usr/bin/env python
#Filename: Day10-02.py

 ###############################################################################################################
#                                                                                                               #
#                               Advent of Code 2021 - Solutions of Problems                                     #
#                                                                                                               #
#   Author:     Marcel Krause                                                                                   #
#   Date:       10.12.2021                                                                                      #
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
|         Day 10 - Riddle 02         |
|                                    |
+------------------------------------+
''')

# Read the input file
with open('Day10-01_input.dat', 'r') as content_file:
    all_lines = [line.rstrip('\n') for line in content_file]

# Matching brackets and error scores for each bracket
matching_pairs = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}
completion_scores = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

# Get the total syntax error score
all_completion_scores = []
for line in all_lines:
    queue = []
    is_legal = True
    completion_score = 0

    for char in line:
        if char in matching_pairs.keys():
            queue.append(char)
            continue
        
        last_element = queue[-1]
        if matching_pairs[last_element] == char:
            queue.pop()
        else:
            is_legal = False
            break
    
    if is_legal:
        completion_queue = list(map(lambda x: matching_pairs[x], queue))
        for item in reversed(completion_queue):
            completion_score *= 5
            completion_score += completion_scores[item]
        all_completion_scores.append(completion_score)

# Get the median completion score
all_completion_scores.sort()
median_completion_score = all_completion_scores[len(all_completion_scores)//2]

# Print the result
print("The median of all completion scores is given by {}.".format(median_completion_score))