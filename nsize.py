n=int(input("enter number of rows and column"))

board_matrix = [[" " for _ in range(n)] for _ in range(n)]

def print_board():
        for i in range(n):
            print(" " + " | ".join(board_matrix[i]))
        if i < n-1:
            print("---+---+---")

def winner():
    
    lines = []
    for i in range(0,n):
         r=[]
         c=[]
         for j in range(0,n):
              r.append(board_matrix[i][j])
              c.append(board_matrix[j][i])
    
         lines.extend([r,c])
    d1=[]
    d2=[]
    for i in range(0,n):
         for j in range(0,n):
              if i==j:
                   d1.append(board_matrix[i][j])
              if (i+j)==n-1:
                   d2.append(board_matrix[i][j]) 
    
    lines.extend([d1,d2])
                      
         
    
    if ["X"] * n in lines:
        print("Player 1 Wins!")
        return True
    if ["O"] * n in lines:
        print("Player 2 Wins!")
        return True
    return False
def draw():
        if all(cell != " " for row in board_matrix for cell in row):
            print("It's a Draw!")

def make_move(value, turn):
    
    m=value-1
    a, b = m//n,m%n 
    if board_matrix[a][b] == " ":  
        if turn == 1:
            board_matrix[a][b] = "X"
        if turn==2:
            board_matrix[a][b] = "O"
    else:
        print("Cell already taken!")
    
    return print_board()

 
def p1():
            print("Player1 Turns!")
            print("Enter a value between(1-9)")
            v=int(input("->"))
            p=1
            l=[v,p]
            
            return l
def p2():
            print("Player2 Turns!")
            print("Enter a value between(1-9)")
            v=int(input("->"))
            p=2
            l=[v,p]
            return l
i=1
while i!=(n**2)+1:
    if i%2==1:
               
        listindex=p1()
        p=make_move(listindex[0],listindex[1])
        
    if i%2==0:
        listindex=p2()
        make_move(listindex[0],listindex[1])
    if winner():
        break
    draw()
    i+=1