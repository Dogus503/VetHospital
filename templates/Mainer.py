WHITE = 1
BLACK = 2


class PieceColor():
    def __init__(self, color):
        self.color = color

    def opponent(self):
        if self.color == WHITE:
            return PieceColor(BLACK)
        return PieceColor(WHITE)

    def is_black(self):
        return self.color == BLACK

    def is_white(self):
        return self.color == WHITE

    def __eq__(self, other):
        return self.color == other.color


def correct_coords(row, col):
    return 0 <= row < 8 and 0 <= col < 8


class Board:

    def __init__(self):
        self.color = WHITE
        self.field = []
        for row in range(8):
            self.field.append([None] * 8)

    def current_player_color(self):
        return self.color

    def cell(self, row, col):
        piece = self.field[row][col]
        if piece is None:
            return '  '
        color = piece.get_color()
        c = 'w' if color == WHITE else 'b'
        return c + piece.char()

    def move_piece(self, row, col, row1, col1):

        if not correct_coords(row, col) or not correct_coords(row1, col1):
            return False
        if row == row1 and col == col1:
            return False
        piece = self.field[row][col]
        if piece is None:
            return False
        if piece.get_color() != self.color:
            return False
        if not piece.can_move(row1, col1):
            return False
        self.field[row][col] = None  # Снять фигуру.
        self.field[row1][col1] = piece  # Поставить на новое место.
        piece.set_position(row1, col1)
        self.color = opponent(self.color)
        return True


class Pawn:

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return 'P'

    def get_color(self):
        return self.color

    def can_move(self, row, col):
        if self.col != col:
            return False
        if self.color == WHITE:
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6
        if self.row + direction == row:
            return True
        if self.row == start_row and self.row + 2 * direction == row:
            return True

        return False


class Knight:
    def __init__(self, row, col, color):
        self.col = col
        self.row = row
        self.color = color

    def get_color(self):
        return self.color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return "N"

    def can_move(self, row, col):
        if 0 <= row <= 7 and 0 <= col <= 7:
            if abs(self.row - row) == 2 and abs(self.col - col) == 1 \
                    or abs(self.row - row) == 1 and abs(self.col - col) == 2:
                return True
        return False


class Bishop:
    def __init__(self, row, col, color):
        self.col = col
        self.row = row
        self.color = color

    def get_color(self):
        return self.color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return "B"

    def can_move(self, row, col):
        if 0 <= row <= 7 and 0 <= col <= 7:
            if abs(self.row - row) == abs(self.col - col):
                return True
        return False


class Queen:
    def __init__(self, row, col, color):
        self.col = col
        self.row = row
        self.color = color

    def get_color(self):
        return self.color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return "Q"

    def can_move(self, row, col):
        if 0 <= row <= 7 and 0 <= col <= 7:
            if abs(self.row - row) == abs(self.col - col) or self.col == col or self.row == row:
                return True
        return False


class Rook:

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return 'R'

    def get_color(self):
        return self.color

    def can_move(self, row, col):
        if self.row != row and self.col != col:
            return False
        return True
