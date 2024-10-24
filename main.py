# Put your function here
def ticTacToe(board):
        #Vertical
        if board[0][0] == board[1][0] == board[2][0]:
            return(board[0][0]) 
        if board[0][1] == board[1][1] == board[2][1]:
             return board[0][1]
        if board[0][2] == board[1][2] == board[2][2]:
                 return board[0][2]
        # Horizontal
        if board[0][0] == board[0][1] == board[0][2]:
              return board[0][0]
        if board[1][0] == board[1][1] == board[1][2]:
              return board[1][0]
        if board[2][0] == board[2][1] == board[1][2]:
              return board[1][0]
        # Diagonal
        if board[0][0] == board[1][1] == board[2][2]:
              return board[0][0]
        if board[0][2] == board[1][1] == board[2][0]:
              return board[0][2]
        else:
            return("Tie") 

# testing
board = [['X','O','O'],['O','X','O'],['X','O','X']]
print(ticTacToe(board))
