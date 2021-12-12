#!/usr/bin/env python
#Filename: Day12-02.py

 ###############################################################################################################
#                                                                                                               #
#                               Advent of Code 2021 - Solutions of Problems                                     #
#                                                                                                               #
#   Author:     Marcel Krause                                                                                   #
#   Date:       12.12.2021                                                                                      #
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
|         Day 12 - Riddle 02         |
|                                    |
+------------------------------------+
''')

# Read the input file
with open('Day12-01_input.dat', 'r') as content_file:
    all_lines = [line.rstrip('\n') for line in content_file]

# Get a map of possible directions
directions = {}
for line in all_lines:
    curr_directions = line.split('-')
    for i in range(2):
        start, end = curr_directions[i], curr_directions[1-i]
        if start in directions.keys():
            directions[start].append(end)
        else:
            directions[start] = [end]

# Starting at the start, generate all possible paths
possible_paths = [["start"]]
small_caves = set()
for curr_path in possible_paths:
    if curr_path[-1] == "end":
        continue
    next_points = directions[curr_path[-1]]
    for next_point in next_points:
        if next_point == "start":
            continue
        if next_point != "end" and 97 <= ord(next_point[0]) <= 122:
            small_caves.add(next_point)
            cave_visited_twice = False
            invalid_path = False
            for small_cave in small_caves:
                if (curr_path + [next_point]).count(small_cave) > 2:
                    invalid_path = True
                    break

                elif (curr_path + [next_point]).count(small_cave) == 2:
                    if cave_visited_twice:
                        invalid_path = True
                        break
                    else:
                        cave_visited_twice = True
            if invalid_path:
                continue
        possible_paths.append(curr_path + [next_point])

# Filter out all non-finished paths
finished_paths = []
for line in possible_paths:
    if line[-1] == "end":
        finished_paths.append(line)
amount_finished_paths = len(finished_paths)

# Print the result
print("There are {} paths through the cave system in which small caves are visited at most once.".format(amount_finished_paths))
