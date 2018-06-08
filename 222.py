board=[0, 1, 2,
       3, 4, 5,
       6, 7, 8 ]

def DrawBoard():
    print("  %s |  %s  | %s " %(board[0], board[1], board[2]))
    print("___|___|___")
    print("  %s |  %s  | %s " %(board[3], board[4], board[5]))
    print("___|___|___")
    print("  %s |  %s  | %s " %(board[6], board[7], board[8]))
    print("___|___|___")
    
DrawBoard()
