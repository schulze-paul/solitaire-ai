import numpy as np
import copy

class GameBoard(): 

    def __init__(self):
        self.board = -128*np.ones((7,7))

        for x_index in range(2,5):
            for y_index in range(0,7):
                self.board[x_index, y_index] = 1
                self.board[y_index, x_index] = 1 

        self.board[3,3] = -1



    def __str__(self):
        pixels = "\n"

        for x_index in range(0,7):
            for y_index in range(0,7):
                pixel_source = self.board[x_index, y_index]
                
                if pixel_source == -128:
                    pixels = pixels + "  "
                if pixel_source == 1:
                    pixels = pixels + " ●"
                if pixel_source == -1:
                    pixels = pixels + " •"
            pixels = pixels + "\n"
        
        return pixels

    def get_possible_moves(self):
        move_locations = []

        for x_index in range(0,5):
            for y_index in range(0,5):

                if all(self.board[x_index, y_index:y_index+3] == [1,1,-1]) or all(self.board[x_index, y_index:y_index+3] == [-1,1,1]):
                    move_location = (x_index, range(y_index,y_index+3))
                    move_locations.append(move_location)
                if all(self.board[x_index:x_index+3, y_index] == [1,1,-1]) or all(self.board[x_index:x_index+3, y_index] == [-1,1,1]):
                    move_location = (range(x_index,x_index+3), y_index)
                    move_locations.append(move_location)

        return move_locations

    def make_move(self, move_location):
        self.board[move_location] = -self.board[move_location]


    def get_new_board_state(self, move_location):
        new_board = copy.deepcopy(self)
        new_board.make_move(move_location)
        #print(new_board)
        return new_board

    def is_perfect(self):
        perfect_board = -128*np.ones((7,7))
        for x_index in range(2,5):
            for y_index in range(0,7):
                perfect_board[x_index, y_index] = -1
                perfect_board[y_index, x_index] = -1 

        perfect_board[3,3] = 1

        if (self.board == perfect_board).all():
            return True
        else: 
            return False
