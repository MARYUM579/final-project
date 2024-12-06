import chess
import chess.svg

def print_board(board):
    print(board)

def is_checkmate(board):
    return board.is_checkmate()

def is_stalemate(board):
    return board.is_stalemate()

def is_check(board):
    return board.is_check()

def is_game_over(board):
    return board.is_game_over()

def get_move():
    move = input("Enter your move (e.g., e2e4): ")
    return move

def play_chess():
    board = chess.Board()
    
    print("Welcome to Chess!")
    print("You play as White. Enter moves in algebraic notation (e.g., e2e4).")
    
    while not is_game_over(board):
        print_board(board)
        
        if board.turn:
            print("White's turn:")
        else:
            print("Black's turn:")
        
        move = get_move()
        
        try:
            board.push(chess.Move.from_uci(move))
        except ValueError:
            print("Invalid move! Try again.")
        
        if is_checkmate(board):
            print("Checkmate!")
            break
        elif is_stalemate(board):
            print("Stalemate!")
            break
        elif is_check(board):
            print("Check!")
        
    print("Game over!")
    print_board(board)

if __name__ == "__main__":
    play_chess()

