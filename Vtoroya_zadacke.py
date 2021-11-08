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




WHITE=1
BLACK=2

row0 = 7
col0 = 3
queen = Queen(row0, col0, BLACK)

print('white' if queen.get_color() == WHITE else 'black')
for row in range(8, -2, -1):
    for col in range(-1, 9):
        if row == row0 and col == col0:
            print(queen.char(), end='')
        elif queen.can_move(row, col):
            print('x', end='')
        else:
            print('-', end='')
    print()