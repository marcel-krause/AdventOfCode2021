#!/usr/bin/env python
#Filename: Day16-02.py

 ###############################################################################################################
#                                                                                                               #
#                               Advent of Code 2021 - Solutions of Problems                                     #
#                                                                                                               #
#   Author:     Marcel Krause                                                                                   #
#   Date:       16.12.2021                                                                                      #
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
|         Day 16 - Riddle 02         |
|                                    |
+------------------------------------+
''')

# Import modules
from functools import reduce


def parse_string(s: str) -> dict:
    # Get the packet version and type ID
    packet_version = int("".join(s[:3]), 2)
    s[:] = s[3:]
    type_id = int("".join(s[:3]), 2)
    s[:] = s[3:]

    # Handle the different type IDs
    if type_id == 4:
        # Handle literal strings
        literal_value = ""
        while True:
            literal_value += "".join(s[1:5])
            value_char = s[0]
            s[:] = s[5:]
            if value_char == "0":
                break
        literal_value_dec = int(literal_value, 2)
        
        return {"version": packet_version, "type_id": type_id, "value": literal_value_dec}
    else:
        # Handle operator strings
        length_type_id = s.pop(0)
        
        if length_type_id == "0":
            # Handle length type 0 strings (the length represents the amount of bits which contain the sub-packets)
            length = int("".join(s[:15]), 2)
            s[:] = s[15:]
            sub_s = s[:length]
            s[:] = s[length:]

            # Iterate over the substring until the length is exhausted
            sub_packet_data = list()
            while len(sub_s) > 0:
                sub_packet_data.append(parse_string(sub_s))

            output = {"version": packet_version, "type_id": type_id, "length_type_id": length_type_id, "length": length, "sub_packets": sub_packet_data}
        else:
            # Handle length type 1 strings (the length represents the amount of sub-packets to follow)
            num_sub_packets = int("".join(s[:11]), 2)
            s[:] = s[11:]

            # Iterate over the number of sub-packets
            sub_packet_data = list()
            for _ in range(num_sub_packets):
                parse_result = parse_string(s)
                sub_packet_data.append(parse_result)

            output = {"version": packet_version, "type_id": type_id, "length_type_id": length_type_id, "num_sub_packets": num_sub_packets, "sub_packets": sub_packet_data}

        return output


def get_packet_value(sub_list: list) -> list[int]:
    sub_sum = []
    for sub_list_element in sub_list:
        if sub_list_element["type_id"] == 4:
            sub_sum_element = sub_list_element["value"]
        elif sub_list_element["type_id"] == 0:
            sub_sum_element = sum(get_packet_value(sub_list_element["sub_packets"]))
        elif sub_list_element["type_id"] == 1:
            sub_sum_element = reduce(lambda x, y: x * y, get_packet_value(sub_list_element["sub_packets"]), 1)
        elif sub_list_element["type_id"] == 2:
            sub_sum_element = min(get_packet_value(sub_list_element["sub_packets"]))
        elif sub_list_element["type_id"] == 3:
            sub_sum_element = max(get_packet_value(sub_list_element["sub_packets"]))
        elif sub_list_element["type_id"] == 5:
            sub_sum_res = get_packet_value(sub_list_element["sub_packets"])
            sub_sum_element = int(sub_sum_res[0] > sub_sum_res[1])
        elif sub_list_element["type_id"] == 6:
            sub_sum_res = get_packet_value(sub_list_element["sub_packets"])
            sub_sum_element = int(sub_sum_res[0] < sub_sum_res[1])
        elif sub_list_element["type_id"] == 7:
            sub_sum_res = get_packet_value(sub_list_element["sub_packets"])
            sub_sum_element = int(sub_sum_res[0] == sub_sum_res[1])

        sub_sum.append(sub_sum_element)

    return sub_sum


# Read the input file
with open('Day16-01_input.dat', 'r') as content_file:
    all_lines = [line.rstrip('\n') for line in content_file]

# Convert the input hex string to a binary string
hex_string = all_lines[0]
binary_string = ""
for c in hex_string:
    binary_string += bin(int(c, 16))[2:].zfill(4)

# Use a list representation in order to modify the binary string globally
s = list(binary_string)

# Decode the packet content
decoded_packet = [parse_string(s)]

# Get the full version sum
full_packet_value = get_packet_value(decoded_packet)[0]

# Print the result
print("The value of the hexadecimal-encoded BITS transmission is {}.".format(full_packet_value))
