#!/usr/bin/env python
#Filename: Day20-01.py

 ###############################################################################################################
#                                                                                                               #
#                               Advent of Code 2021 - Solutions of Problems                                     #
#                                                                                                               #
#   Author:     Marcel Krause                                                                                   #
#   Date:       20.12.2021                                                                                      #
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
|         Day 20 - Riddle 01         |
|                                    |
+------------------------------------+
''')

# Read the input file
with open('Day20-01_input.dat', 'r') as content_file:
    all_lines = [line.rstrip('\n') for line in content_file]

# Get the enhancement algorithm and the raw input image from the input
enhancement_algorithm = all_lines[0]
input_image_raw = all_lines[2:]

# Convert the input image to a matrix
input_image = []
for line in input_image_raw:
    input_image.append(list(line))

# Add an additional 3 pixel wide border around the input image to adjust for the actual infinite size of the input image
additional_chars = 3
top_bottom = ["."]*(2*additional_chars + len(input_image))
new_input_image = [top_bottom.copy() for _ in range(additional_chars)]
for line in input_image:
    new_input_image.append(["."]*additional_chars + list(line) + ["."]*additional_chars)
for _ in range(additional_chars):
    new_input_image.append(top_bottom)

# Perform the iterations of the image enhancement
enhancement_iterations = 2
for step in range(enhancement_iterations):

    # Initialize the new output image
    output_image = [ ["." for _ in range(len(new_input_image))] for _ in range(len(new_input_image)) ]

    # Scan through the current input image and perform the image enhancement
    for row in range(1, len(new_input_image)-1):
        for col in range(1, len(new_input_image[row])-1):

            # Get the neighbors of the current pixel (including the pixel itself)
            neighbor_points = []
            for i in range(-1, 2):
                for j in range(-1, 2):
                    neighbor_points.append( (row + i, col+j) )
            
            # Calculate the current pixel enhancement value by building a binary number from the pixel and its neighbors
            pixel_enhancement_value = ""
            for neighbor in neighbor_points:
                pixel_enhancement_value += new_input_image[neighbor[0]][neighbor[1]]
            enhancement_index = int(pixel_enhancement_value.replace("#", "1").replace(".", "0"), 2)

            # Set the current pixel to its new value according to the enhancement algorithm
            output_pixel = enhancement_algorithm[enhancement_index]
            output_image[row][col] = output_pixel

    # Adjust for the infinite size of the grid by correcting the borders of the current image
    replacement_pixel = output_image[1][1]
    for row in range(len(output_image)):
        if row == 0 or row == len(output_image)-1:
            col_range = range(len(output_image[0]))
        else:
            col_range = [0, len(output_image[0])-1]

        for col in col_range:
            output_image[row][col] = replacement_pixel

    # Extend the image by one pixel on each side
    if step < enhancement_iterations-1:
        additional_chars = 1
        top_bottom = [replacement_pixel]*(2 + len(output_image))
        new_input_image = [top_bottom.copy()].copy()
        for line in output_image:
            new_input_image.append([replacement_pixel] + line + [replacement_pixel])
        new_input_image.append(top_bottom)

# Count all lit pixels
lit_pixel_count = 0
for row in output_image:
    for pixel in row:
        if pixel == "#":
            lit_pixel_count += 1

# Print the result
print("After {} iterations, there are {} lit pixels in the output image.".format(enhancement_iterations, lit_pixel_count))
