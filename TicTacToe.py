class TicTacToe:

    def __init__(self):
        self.diag = 0
        self.anti_diag = 0
        self.cols = [0 for _ in range(3)]
        self.rows = [0 for _ in range(3)]
        self.matrix = [' ' for _ in range(9)]

    def make_move(self, player, col, row) -> int:

        self.cols[col] += player
        self.rows[row] += player
        if row == col: self.diag += player
        if row + col == 2: self.anti_diag += player

        self.matrix[col + (3 * row)] = 'X' if player == 1 else 'O'
        if self.diag == 3 or self.diag == -3:
            return player
        if self.anti_diag == 3 or self.anti_diag == -3:
            return player
        for x in range(3):
            if self.cols[x] == 3 or self.rows[x] == 3 or self.cols[x] == -3 or self.rows[x] == -3:
                return player

        return 0
    def print_matrix(self):
        for x in range(len(self.matrix)):
            print("|" + self.matrix[x] + "|", end= "")
            if (x+1)%3 == 0: print("\n")
if __name__ == "__main__":
    TTT = TicTacToe()

    gamestate = 0
    currentPlayer = 1
    TTT.print_matrix()
    while(gamestate == 0):
        col, row = tuple(int(x) for x in input("Enter col and row: ").split())
        gamestate = TTT.make_move(currentPlayer, col, row)
        TTT.print_matrix()
        currentPlayer = currentPlayer * -1

        