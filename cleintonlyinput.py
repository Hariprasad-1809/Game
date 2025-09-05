import socket

def client():
    s1 = socket.socket()
    s1.connect(('localhost', 12345))

    while True:
        
        data = s1.recv(4096).decode()
        if not data:
            print("Server disconnected!")
            break

        *board_lines, status = data.split("\n")
        board = "\n".join(board_lines)

        print("\nCurrent Board:")
        print(board)
        if status == "WIN_X":
            print("Player 1 (X) wins!")
            break
        elif status == "WIN_O":
            print("Player 2 (O) wins!")
            break
        elif status == "DRAW":
            print("It is a Draw!")
            break
        if status in ("YOUR_TURN", "INVALID"):
            move = int(input("Your Turn (O): "))
            s1.send(str(move).encode())
        elif status == "WAIT":
            print("Waiting for player 1")
            continue

    s1.close()


if __name__ == "__main__":
    client()
