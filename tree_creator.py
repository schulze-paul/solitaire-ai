
from game_board import GameBoard

game_number = 1

class GameState():

    def __init__(self, move, board_state, previous_game_state):
        self.move = move
        self.board_state = board_state
        self.previous_game_state = previous_game_state

        # calculate possible moves
        self.possible_moves = board_state.get_possible_moves()

    def is_final_game_state(self):
        if len(self.possible_moves) > 0:
            return False
        else:
            return True


    def grow_branches(self):
        # create new branches
        self.subsequent_game_states = []

        # find the new board state and game state for each possible move 
        for move in self.possible_moves:
            subsequent_board_state = self.board_state.get_new_board_state(move)
            subsequent_game_state = GameState(move, subsequent_board_state, self)
            self.subsequent_game_states.append(subsequent_game_state)

        # check if any new branches from the new game states
        if all([game_state.is_final_game_state() for game_state in self.subsequent_game_states]):
            return

        # grow the new branches
        for game_state in self.subsequent_game_states:
            if game_state.is_final_game_state():
                global game_number
                with open("log.txt", "a") as log_file:
                    log_file.write("Game Number: " + str(game_number))
                    log_file.write(str(game_state.board_state))
                print("Game Number ", game_number, "finished.")
                print(game_state.board_state)
                if (game_state.board_state.is_perfect()):
                    print("A Perfect Game!")
                game_number = game_number + 1

            if not game_state.is_final_game_state():
                game_state.grow_branches()


game_board = GameBoard()

game_state = GameState(None, game_board, None)

game_state.grow_branches()