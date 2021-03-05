"""
This class is responsible for storing all the information about the current state of the chess game.
It is also responsible for detrmining the valid moves at the current state.
"""
class GameState():
    def _init_(self):
        self.board = [
            []
        ]