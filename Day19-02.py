#!/usr/bin/env python
#Filename: Day19-02.py

 ###############################################################################################################
#                                                                                                               #
#                               Advent of Code 2021 - Solutions of Problems                                     #
#                                                                                                               #
#   Author:     Marcel Krause                                                                                   #
#   Date:       19.12.2021                                                                                      #
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
|         Day 19 - Riddle 02         |
|                                    |
+------------------------------------+
''')


def find_overlaps(ref_list, list_2) -> tuple[list, set]:
    permutations = {
        (0,1,2): 1,
        (1,2,0): 1,
        (2,0,1): 1,
        (2,1,0): -1,
        (1,0,2): -1,
        (0,2,1): -1
    }

    # Consider all rotations and coordinate transformations without changing the handedness of the coordinate system (i.e. no mirroring)
    for x in range(1,-2,-2):
        for y in range(1,-2,-2):
            for z in range(1,-2,-2):
                for permutation, parity in permutations.items():
                    # In case the parity does not match, consider the next coordinate transformation
                    if x*y*z*parity != 1:
                        continue

                    # Transform the coordinates of the second list
                    curr_scanner_result_list = []
                    for point in list_2:
                        new_point = [0,0,0]
                        multiplicator = [x,y,z]
                        for i in range(len(point)):
                            new_point[permutation[i]] = point[i]*multiplicator[i]
                        curr_scanner_result_list.append(new_point)

                    # Move any point in the transformed second list to any point in the reference list
                    for point in curr_scanner_result_list:
                        for ref_point in ref_list:
                            scanner_position = []
                            for i in range(len(point)):
                                scanner_position.append(ref_point[i] - point[i])

                            # Move the points to the current reference point
                            match_count = 0
                            transformed_points = set()
                            for old_point in curr_scanner_result_list:
                                new_point = []
                                for i in range(len(old_point)):
                                    new_point.append(old_point[i] + scanner_position[i])
                                new_point = tuple(new_point)
                                transformed_points.add(new_point)
                                if new_point in ref_list:
                                    match_count += 1
                            
                            # In case we find 12 overlapping points in this transformed system, we actually found two scanners that are in reach of each other
                            if match_count == 12:
                                return scanner_position, transformed_points
    return [], []


def get_squared_euclidean_distance(coordinates1: list[int], coordinates2: list[int]) -> int:
    return sum([(coordinates1[i] - coordinates2[i])**2 for i in range(len(coordinates1))])


def get_manhattan_distance(coordinates1: list, coordinates2: list) -> int:
    return sum([abs(coordinates1[i] - coordinates2[i]) for i in range(len(coordinates1))])


# Read the input file
with open('Day19-01_input.dat', 'r') as content_file:
    all_lines = [line.rstrip('\n') for line in content_file]

# Get all scanner results from the input file
scanner_result_list = {}
curr_scanner = None
for line in all_lines:
    if "scanner" in line:
        curr_scanner = int(line.replace("--- scanner ", "").split()[0])
        scanner_result_list[curr_scanner] = set()
    elif "," in line:
        scanner_result_list[curr_scanner].add(tuple(map(lambda x: int(x), line.split(","))))

# For each scanner, calculate the squared Euclidean distance between each point as an invariance metric
scanner_result_list_distances = {}
for key, val in scanner_result_list.items():
    all_distances = set()
    for point1 in val:
        for point2 in val:
            if point1 == point2:
                continue
            all_distances.add(get_squared_euclidean_distance(point1, point2))
    scanner_result_list_distances[key] = all_distances

# Find likely pairs of scanners with at least twelve points with the same distance mutual distances of the points in the set
scanner_pair_mapping = {}
for i in range(len(scanner_result_list_distances)):
    for j in range(1, len(scanner_result_list_distances)):
        if i == j:
            continue
        if len(scanner_result_list_distances[i].intersection(scanner_result_list_distances[j])) >= 66:
            if i in scanner_pair_mapping:
                scanner_pair_mapping[i].append(j)
            else:
                scanner_pair_mapping[i] = [j]

# Create a queue of scanner pairs which will be checked
remaining_scanners = set(range(1, len(scanner_result_list))) - set(scanner_pair_mapping[0])
scanner_queue = {0: scanner_pair_mapping[0]}
next_scanners_to_consider = scanner_pair_mapping[0].copy()
while len(next_scanners_to_consider) > 0:
    temp_next_scanners = []
    for next_scanner_to_consider in next_scanners_to_consider:
        temp = []
        for scanner in scanner_pair_mapping[next_scanner_to_consider]:
            if scanner in remaining_scanners:
                temp.append(scanner)
                remaining_scanners.remove(scanner)
        if len(temp) > 0:
            scanner_queue[next_scanner_to_consider] = temp[:]
        temp_next_scanners += temp
    next_scanners_to_consider = temp_next_scanners.copy()

# Prepare the list of scanner and beacon positions
scanner_positions = {0: [0,0,0]}
beacon_positions = set()
for beacon_position in scanner_result_list[0]:
    beacon_positions.add(tuple(beacon_position))

# Check the scanner queue for actual overlapping scanners
for scanner1 in scanner_queue.keys():
    for scanner2 in scanner_queue[scanner1]:

        # Search for overlaps between the two scanners
        scanner_positions[scanner2], transformed_points = find_overlaps(scanner_result_list[scanner1], scanner_result_list[scanner2])

        # No overlaps found
        if len(scanner_positions[scanner2]) == 0:
            continue

        # Save the beacon and scanner positions
        scanner_result_list[scanner2] = transformed_points
        for beacon_position in transformed_points:
            beacon_positions.add(tuple(beacon_position))

# Get the result
max_manhattan_distance = 0
for scanner1 in range(len(scanner_result_list)):
    for scanner2 in range(scanner1+1, len(scanner_result_list)):
        curr_manhattan_distance = get_manhattan_distance(scanner_positions[scanner1], scanner_positions[scanner2])
        if curr_manhattan_distance > max_manhattan_distance:
            max_manhattan_distance = curr_manhattan_distance

# Print the result
print("The maximum Manhattan distance of two scanners is {}.".format(max_manhattan_distance))
