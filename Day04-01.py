#!/usr/bin/env python
#Filename: Day04-01.py

 ###############################################################################################################
#                                                                                                               #
#                               Advent of Code 2021 - Solutions of Problems                                     #
#                                                                                                               #
#   Author:     Marcel Krause                                                                                   #
#   Date:       04.12.2021                                                                                      #
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
|         Day 04 - Riddle 01         |
|                                    |
+------------------------------------+
''')

class bingo_board():
    def __init__(self, board_config):
        self.board_config = board_config
        self.played_numbers = [ [0 for _ in range(len(board_config[0]))] for _ in range(len(board_config[0]))]
    
    def print_board(self):
        for line in self.board_config:
            print(line)

    def print_played_numbers(self):
        for line in self.played_numbers:
            print(line)

    def check_number(self, num):
        for i in range(len(self.board_config)):
            for j in range(len(self.board_config[0])):
                if self.board_config[i][j] == num:
                    self.played_numbers[i][j] = 1
    
    def check_for_bingo(self):
        target_count = len(self.board_config[0])
        col_count = [0 for _ in range(target_count)]
        for i in range(len(self.played_numbers)):
            row_count = 0
            for j in range(len(self.played_numbers[0])):
                row_count += self.played_numbers[i][j]
                col_count[j] += self.played_numbers[i][j]
                if col_count[j] == target_count:
                    return True
            if row_count == target_count:
                return True
        
        return False
    
    def get_score(self):
        total_score = 0
        for i in range(len(self.played_numbers)):
            for j in range(len(self.played_numbers[0])):
                if self.played_numbers[i][j] == 0:
                    total_score += self.board_config[i][j]
        return total_score

# Read the input file and fill the boards
with open('Day04-01_input.dat', 'r') as content_file:
    drawn_numbers = list(map(lambda x: int(x), content_file.readline().rstrip('\n').split(',')))
    content_file.readline()

    board_config = []
    all_boards = []
    for line in content_file.readlines():
        if line.rstrip('\n') == '':
            all_boards.append(bingo_board(board_config))
            board_config = []
            continue
        
        board_config.append(list(map(lambda x: int(x), line.rstrip('\n').split())))
    all_boards.append(bingo_board(board_config))

# Draw the numbers and play all boards
game_over = False
for num in drawn_numbers:
    for board in all_boards:
        board.check_number(num)
        if board.check_for_bingo():
            final_score = board.get_score() * num
            game_over = True
            break
    if game_over:
        break


# Print the result
print("The final score of the winning board is given by {}.".format(final_score))
