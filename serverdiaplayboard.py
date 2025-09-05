import socket
class tictactoe:
    def __init__(self, n):
        self.n = n
        self.board = []
        x = 1
        for i in range(n):
            row = []
            for j in range(n):
                row.append(str(x))
                x += 1
            self.board.append(row)

    def print_board(self):
        b=""
        for i in range(self.n):
            b+=" " + " | ".join(self.board[i])+"\n"
            if i < self.n - 1:
                b+="---+" * (self.n - 1) + "---\n"
        return b
    def make_move(self, value, symbol):
        m = value - 1
        a, b = divmod(m, self.n)
        numbers = [str(i) for i in range(1, self.n * self.n + 1)]
        if self.board[a][b] in numbers:
            self.board[a][b] = symbol
            self.print_board()
            return True
        else:
            print("Cell already taken!")
            return False

    def check_winner(self, symbol):
        for r in self.board:
            if all(i == symbol for i in r):
                return True

        for c in range(self.n):
            if all(self.board[i][c] == symbol for i in range(self.n)):
                return True

        if all(self.board[i][i] == symbol for i in range(self.n)) or all(self.board[i][self.n - 1 - i] == symbol for i in range(self.n)):
            return True

        return False

    def is_draw(self):
        numbers = [str(i) for i in range(1, self.n * self.n + 1)]
        return all(cell not in numbers for row in self.board for cell in row)


def server():
    n = int(input("Enter Board size: "))
    g = tictactoe(n)
    s = socket.socket()
    s.bind(('localhost', 12345))
    s.listen(1)
    print("Waiting for client!")
    c, addr = s.accept()
    turn = 1
    i = 1
    while i <= n ** 2:
        if turn == 1:
            v = int(input("Your Turn (X):"))
            if g.make_move(v, "X"):
                b=g.print_board()
                print(b)
                if g.check_winner("X"):
                    c.sendall((b + "\nWIN_X").encode())
                    print("Player 1 Wins!")
                    break
                elif g.is_draw():
                    c.sendall((b + "\nDRAW").encode())
                    print("It is a Draw!")
                    break
                else:
                    
                    c.sendall((b + "\nYOUR_TURN").encode())
                turn = 2
                
               
                
            else:
                print("Cell already taken!.")
          
                continue
            turn=2  
            
        else:
            print("Waiting for Player 2(O)!")
             
            v = c.recv(1024).decode()
            if not v:  
                print("Client disconnected!")
                break
            try:
                v = int(v)
            except ValueError:
                print(f"Invalid data received from client: {v}")
                continue
            if g.make_move(v, "O"):
                b=g.print_board()
                print(b)
                if g.check_winner("O"):
                    c.sendall((b + "\nWIN_O").encode())
                    print("Player 2 Wins!")
                    break
                elif g.is_draw():
                    c.sendall((b + "\nDRAW").encode())
                    print("It is a Draw!")
                    break
                else:
                    
                    c.sendall((b + "\nWAIT").encode())
                turn = 1
            else:
                c.sendall((g.print_board() + "\nINVALID").encode())
                continue
            
        i += 1
    c.close()

if __name__ == "__main__":
    server()
