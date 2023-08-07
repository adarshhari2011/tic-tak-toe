board={1:" ",2:" ",3:" ",4:" ",5:" ",6:" ",7:" ",8:" ",9:" "}
def draw():
    print(f"{board[1]}|{board[2]}|{board[3]}")
    print("-+-+-")
    print(f"{board[4]}|{board[5]}|{board[6]}")
    print("-+-+-")
    print(f"{board[7]}|{board[8]}|{board[9]}")
def check_winner():
    if board[1]=="X" and board[2]=="X" and board[3]=="X":
        print("winner is X")
    elif board[1]=="O" and board[2]=="O" and board[3]=="O":
        print("winner is O")
    elif board[4]=="X" and board[5]=="X" and board[6]=="X":
        print("winner is X")
    elif board[4]=="O" and board[5]=="O" and board[6]=="O":
        print("winner is O")
    elif board[7]=="X" and board[8]=="X" and board[9]=="X":
        print("winner is X")
    elif board[7]=="O" and board[8]=="O" and board[9]=="O":
        print("winner is O")
    elif board[1]=="X" and board[4]=="X" and board[7]=="X":
        print("winner is X")
    elif board[1]=="O" and board[4]=="O" and board[7]=="O":
        print("winner is O")
    elif board[2]=="X" and board[5]=="X" and board[8]=="X":
        print("winner is X")
    elif board[2]=="O" and board[5]=="O" and board[8]=="O":
        print("winner is O")
    elif board[3]=="X" and board[6]=="X" and board[9]=="X":
        print("winner is X")
    elif board[3]=="O" and board[6]=="O" and board[9]=="O":
        print("winner is O")
    elif board[1]=="X" and board[5]=="X" and board[9]=="X":
        print("winner is X")
    elif board[1]=="O" and board[5]=="O" and board[9]=="O":
        print("winner is O")
    elif board[3]=="X" and board[5]=="X" and board[7]=="X":
        print("winner is X")
    elif board[3]=="O" and board[5]=="O" and board[7]=="O":
        print("winner is O")
A=0
while True:
    if A==0:
        position=int(input("pick a position:"))
        board[position]="X"
        draw()
        check_winner()
        A=1
    elif A==1:
        position=int(input("pick a position:"))
        board[position]="O"
        draw()
        check_winner()
        A=0

