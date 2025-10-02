# print player 0's turn
# input enter row(1,3): 
# input enter col(1,3):
# print board
# player X's turn
# input enter row(1,3): 
# input enter col(1,3):




board = """
 ___________
|   |   |   |
|---|---|---|
|   |   |   |
|---|---|---|
|___|___|___|

"""
board_list = list(board)

while True:
    print("player 0's turn")
    a1 = int(input("enter row(1,3) :"))
    a2 = int(input("enter col(1,3) :"))
    if a1 == 1 and a2 == 1:
       board_list[16] = "0"
    elif a1 == 1 and a2 == 2:
       board_list[20] = "0"
    elif a1 == 1 and a2 == 3:
       board_list[24] = "0"
    elif a1 == 2 and a2 == 1:
       board_list[44] = "0"
    elif a1 == 2 and a2 == 2:
       board_list[48] = "0"
    elif a1 == 2 and a2 == 3:
       board_list[52] = "0"
    elif a1 == 3 and a2 == 1:
       board_list[72] = "0"
    elif a1 == 3 and a2 == 2:
       board_list[76] = "0"
    elif a1 == 3 and a2 == 3:
       board_list[80] = "0"
    board = "".join(board_list)
    print(board)
    if board_list[16]==board_list[20]==board_list[24] == "0":
       print("congratulations you won")
    elif board_list[44]==board_list[48] == board_list[52] == "0":
       print("congratulations you won")
    elif board_list[72]==board_list[76]== board_list[80] == "0":
       print("congratulations you won")
    elif board_list[16]==board_list[48]== board_list[80] == "0":
       print("congratulations you won")
    elif board_list[72]==board_list[48]==board_list[24] == "0":
       print("congratulations you won")
    elif (board_list[16] in ["0","X"] and
    board_list[20] in ["0","X"] and
    board_list[24] in ["0","X"] and
    board_list[44] in ["0","X"] and
    board_list[48] in ["0","X"] and
    board_list[52] in ["0","X"] and
    board_list[72] in ["0","X"] and
    board_list[76] in ["0","X"] and
    board_list[80] in ["0","X"]):
       print("It's a draw!")


    print("player X's turn")
    b1 = int(input("enter row(1,3) :"))
    b2 = int(input("enter col(1,3) :"))
    if b1 == 1 and b2 == 1:
       board_list[16] = "X"
    elif b1 == 1 and b2 == 2:
       board_list[20] = "X"
    elif b1 == 1 and b2 == 3:
       board_list[24] = "X"
    elif b1 == 2 and b2 == 1:
       board_list[44] = "X"
    elif b1 == 2 and b2 == 2:
       board_list[48] = "X"
    elif b1 == 2 and b2 == 3:
       board_list[52] = "X"
    elif b1 == 3 and b2 == 1:
       board_list[72] = "X"
    elif b1 == 3 and b2 == 2:
       board_list[76] = "X"
    elif b1 == 3 and b2 == 3:
       board_list[80] = "X"   
    board = "".join(board_list)
    print(board)  
    if board_list[16]==board_list[20]==board_list[24] == "X":
       print("congratulations you won")
    elif board_list[44]==board_list[48] == board_list[52] == "X":
       print("congratulations you won")
    elif board_list[72]==board_list[76]== board_list[80] == "X":
       print("congratulations you won")
    elif board_list[16]==board_list[48]== board_list[80] == "X":
       print("congratulations you won")
    elif board_list[72]==board_list[48]==board_list[24] == "X":
       print("congratulations you won")
    elif (board_list[16] in ["0","X"] and
    board_list[20] in ["0","X"] and
    board_list[24] in ["0","X"] and
    board_list[44] in ["0","X"] and
    board_list[48] in ["0","X"] and
    board_list[52] in ["0","X"] and
    board_list[72] in ["0","X"] and
    board_list[76] in ["0","X"] and
    board_list[80] in ["0","X"]):
       print("It's a draw!")