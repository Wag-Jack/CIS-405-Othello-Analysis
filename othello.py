import constants as c

class Board:
    def __init__(self):
        # Creating initial blank board
        self.board = list()
        for i in range(8):
            self.board.append(list())
            for _ in range(8):
                self.board[i].append(c.N)

        # Creating initial disc setup on board
        # WB
        # BW
        self.board[3][3] = c.W
        self.board[3][4] = c.B
        self.board[4][3] = c.B
        self.board[4][4] = c.W

    # Place piece on board
    # (Add in functionality about legal moves once implemented)
    def set_piece(self, color, i, j):
        if color in c.options.keys() and i in range(8) and j in range(8):
            self.board[i][j] = color

    def get_piece(self, i, j):
        if i in range(8) and j in range(8):
            return self.board[i][j]
        return None

    def print_board(self):
        for i in range(8):
            for j in range(8):
                piece = self.get_piece(i, j)
                print(c.options[piece], end=' ')
            print()

    def outflank(self):
        pass

    def check_legal_move(self, i, j):
        pass

    def check_current_leader(self):
        pass

    def game_status(self):
        pass