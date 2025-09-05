class Board:
    def __init__(self, n):
        self.n = n
        self.board=[]
        x = 1
        for i in range(n):
            row=[]
            for j in range(n):
                row.append(str(x))
                x+=1
            self.board.append(row)

    def print_board(self):
        for i in range(self.n):
            print(" " + " | ".join(self.board[i]))         
            if i < self.n - 1:
                print("---+" * (self.n - 1) + "---")

    def make_move(self, value, symbol):
        m = value - 1
        a, b = divmod(m, self.n)
        n=self.n
        numbers=[str(i) for i in range(n*n)]
        if self.board[a][b] in numbers:
            self.board[a][b] = symbol
            self.print_board()
            return True
        else:
            print("Cell already taken!")
            return False

    def check_winner(self, symbol):
        n = self.n
        for r in self.board:
            if all(i == symbol for i in r):
                return True

        for c in range(n):
            if all(self.board[i][c] == symbol for i in range(n)):
                return True

        if all(self.board[i][i] == symbol for i in range(n)) or all(self.board[i][n - 1 - i] == symbol for i in range(n)):
            return True
        return False


    def is_draw(self):
        n=self.n
        numbers=[str(i) for i in range(n*n)]
        return all(cell not in  numbers for row in self.board for cell in row)


class Player1:
    def __init__(self, symbol="X"):
        self.symbol = symbol

    def get_move(self, n):
        while True:
            try:
                value = int(input(f"Player 1 ({self.symbol}) - Enter a value between 1 and {n*n}: "))
                if 1 <= value <= n * n:
                    return value
                else:
                    print("Invalid input. Try again.")
            except ValueError:
                print("Enter a valid number.")


class Player2:
    def __init__(self, symbol="O"):
        self.symbol = symbol

    def get_move(self, n):
        while True:
            try:
                value = int(input(f"Player 2 ({self.symbol}) - Enter a value between 1 and {n*n}: "))
                if 1 <= value <= n * n:
                    return value
                else:
                    print("Invalid input. Try again.")
            except ValueError:
                print("Enter a valid number.")



def main():
    n = int(input("Enter number of rows and columns: "))
    board = Board(n)
    player1 = Player1()
    player2 = Player2()

    board.print_board()
    for turn in range(1, n*n + 1):
        current_player = player1 if turn % 2 == 1 else player2
        move = current_player.get_move(n)
        if not board.make_move(move, current_player.symbol):
            continue  

        if board.check_winner(current_player.symbol):
            print(f"{'Player 1' if turn % 2 == 1 else 'Player 2'} Wins!")
            break

        if board.is_draw():
            print("It's a Draw!")
            break
    
main()