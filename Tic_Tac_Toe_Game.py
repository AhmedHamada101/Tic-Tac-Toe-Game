# Show Board
def show_board(board):
    for row in board:
        for col in row:
            print(col, end='\t')
        print('\n')

# Set Players
def set_players():
    from random import choice
    player1 = choice(['X','O'])
    if player1 == 'O':
        player2 = 'X' 
    else:
        player2 ='O' 
    return player1, player2

# Take Input
def take_input(board, player):
    while True:
        player_input = input('Please Enter a number between 1,9 represents an empty position:     ')
        if player_input == '1' and board[0][0].isdigit() :
            board[0][0] = player
            break
        elif player_input == '2' and board[0][1].isdigit():
            board[0][1] = player
            break
        elif player_input == '3' and board[0][2].isdigit():
            board[0][2] = player
            break
        elif player_input == '4' and board[1][0].isdigit():
            board[1][0] = player
            break
        elif player_input == '5' and board[1][1].isdigit():
            board[1][1] = player
            break
        elif player_input == '6' and board[1][2].isdigit():
            board[1][2] = player
            break
        elif player_input == '7' and board[2][0].isdigit():
            board[2][0] = player
            break
        elif player_input == '8' and board[2][1].isdigit():
            board[2][1] = player
            break
        elif player_input == '9' and board[2][2].isdigit():
            board[2][2] = player
            break
        else:
            print('Invalid Choice') 
            continue 
    show_board(board)

# Check Full Board
def check_full_board(board):
    for row in board:
        for col in row:
            if col.isdigit():
                return False
    return True

#Check Win
def check_win(board):
    return board[0][0] == board[0][1] == board[0][2] or \
           board[1][0] == board[1][1] == board[1][2] or \
           board[2][0] == board[2][1] == board[2][2] or \
           board[0][0] == board[1][0] == board[2][0] or \
           board[0][1] == board[1][1] == board[2][1] or \
           board[0][2] == board[1][2] == board[2][2] or \
           board[0][0] == board[1][1] == board[2][2] or \
           board[0][2] == board[1][1] == board[2][0]       

# Start Playing
def start_playing():
    player1, player2 = set_players()
    print("Player1 :  ", player1)
    print("Player2 :  ", player2, '\n')
    
    board = [['1','2','3'],
             ['4','5','6'],
             ['7','8','9']]
    show_board(board)
    
    while True:
        for player in [player1, player2]:
            print(f"{player} turn")
            take_input(board, player)
            if check_win(board):
                print(f"{player} wins")
                break
            if check_full_board(board):
                print('Game Finished. Draw!')
                break
        if check_win(board):
            break
        if check_full_board(board):
            break    

# Play Again
def play_again():
    while True:
        play_again = input("To play again enter [1] and to not play again enter [0]  ===>  \n")
        if play_again in ['0', '1']:
            play_again = int(play_again)
            break
        else:
            print('Invalid Choice! Please choose 0 or 1')
            continue
    return play_again

# Let's Play
def play():
    while True:
        start_playing()
        if play_again() == 1:
            continue
        else:
            print('END')
            break

if __name__ == '__main__':
    play()