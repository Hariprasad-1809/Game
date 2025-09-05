import socket

n = int(input("Enter board size n: "))
board_matrix = [[" " for _ in range(n)] for _ in range(n)]

def print_board():
    for i in range(n):
        print(" " + " | ".join(board_matrix[i]))
        if i < n - 1:
            print("---+" * (n - 1) + "---")

def winner():
    lines = []
    for i in range(n):
        r = [board_matrix[i][j] for j in range(n)]
        c = [board_matrix[j][i] for j in range(n)]
        lines.extend([r, c])
    d1 = [board_matrix[i][i] for i in range(n)]
    d2 = [board_matrix[i][n - i - 1] for i in range(n)]
    lines.extend([d1, d2])
    if ["X"] * n in lines:
        print("Player 1 (X) Wins!")
        return True
    if ["O"] * n in lines:
        print("Player 2 (O) Wins!")
        return True
    return False

def draw():
    if all(cell != " " for row in board_matrix for cell in row):
        print("It's a Draw!")
        return True
    return False

def make_move(value, turn):
    m = value - 1
    a, b = m // n, m % n
    if board_matrix[a][b] == " ":
        board_matrix[a][b] = "X" if turn == 1 else "O"
        return True
    return False

s = socket.socket()
s.bind(("localhost", 9999))
s.listen(1)
print("Waiting for client to connect...")
conn, addr = s.accept()
print(f"Connected to {addr}")
conn.send(str(n).encode())
client_n = int(conn.recv(1024).decode())
if client_n != n:
    print("Board size mismatch")
    conn.close()
    exit()

i = 1
while i <= n ** 2:
    if i % 2 == 1:
        v = int(input("Your turn (X): "))
        m = v - 1
        a, b = m // n, m % n
        if board_matrix[a][b] != " ":
            print("Cell already taken. You lose your turn.")
            conn.send(str(-1).encode())
        else:
            make_move(v, 1)
            conn.send(str(v).encode())
        print_board()
        if winner() or draw():
            break
        i += 1
    else:
        print("Waiting for Player 2...")
        v = conn.recv(1024).decode()
        v = int(v)
        if v != -1:
            make_move(v, 2)
        else:
            print("Player 2 made an invalid move. Skipping their turn.")
        print_board()
        if winner() or draw():
            break
        i += 1

conn.close()