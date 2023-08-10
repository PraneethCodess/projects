# Here we are going to create an interactive tic tac toe project.
import random


# function to DISPLAY THE BOARD
def display_board(board):
    print('                    ' + board[1] + '|' + board[2] + '|' + board[3])
    print('                  ----------')
    print('                    ' + board[4] + '|' + board[5] + '|' + board[6])
    print('                  -----------')
    print('                    ' + board[7] + '|' + board[8] + '|' + board[9])


# function to take PLAYER INPUT AS X OR O
def player_input():
    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input('Player 1 please choose a marker X or O: ').upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


# STEP 3- A function to board list a marker and desired position to place and assign it to board
def place_marker(board, marker, position):
    board[position] = marker


# STEP 4- Function to check after marker did player win the game.
def win_check(board, mark):
    # condition to win: i) all columns must be of same marker  ii) rows should be of same marker  iii) diagonals
    # should be of same marker.

    # i) columns:
    if ((board[1] == mark and board[2] == mark and board[3] == mark) or (
            board[4] == mark and board[5] == mark and board[6] == mark) or (
            board[7] == mark and board[8] == mark and board[9] == mark)):
        return True
    # ii) rows:
    elif ((board[1] == mark and board[4] == mark and board[7] == mark) or (
            board[2] == mark and board[5] == mark and board[8] == mark) or (
                  board[3] == mark and board[6] == mark and board[9] == mark)):
        return True
    # iii) diagonals:
    elif ((board[1] == mark and board[5] == mark and board[9] == mark) or (
            board[3] == mark and board[5] == mark and board[7] == mark)):
        return True

    else:
        return False


# STEP 5- Using random function we decide which player goes first:
def toss():
    flip = random.randint(0, 1)

    if flip == 0:
        return 'Player 1'

    else:
        return 'Player 2'


# STEP 6- Check if space is available at given position:

def space_check(board, position):
    if board[position] == ' ':
        return True
    else:
        return False


# STEP 7- Check if board is full

def check_boardfull(board):
    for i in range(1, 10):
        if space_check(board, i) == True:
            return False

    return True


# STEP 8- function to ask player position for next move and use step 6 if that place is empty:
def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your position (1-9): '))

    return position


# STEP 9- function asking if player wants to play again:

def replay():
    response = input('Want to play again: YES or NO: ').upper()

    if response == 'YES':
        return True
    else:
        return False


# STEP 10- Main block of code for the whole game:

# Use WHILE loop to keep running the game

print('WELCOME TO TIC TAC TOE GAME :) :) ')

while True:

    # PLAY THE GAME

    # Initially we set up the game (board , who is first, choose markers X & O)

    the_board = [' '] * 10
    player1_marker, player2_marker = player_input()
    print('Lets go for a Toss')
    turn = toss()
    print(turn + ' will go first')

    play_game = input('Ready to go Y or N: ').upper()

    if play_game == 'Y':
        game_on = True
    else:
        game_on = False

    # GAME PLAY
    while game_on:

        if turn == 'Player 1':
            # first we display the empty board

            display_board(the_board)

            # choose the position

            position = player_choice(the_board)

            # Place thw marker in the position
            place_marker(the_board, player1_marker, position)

            # check if placing it is a win
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Yoho!! Congratulations PLAYER 1 has WON ')
                game_on = False

            else:
                if check_boardfull(the_board):
                    display_board(the_board)
                    print('THE GAME HAS TIED !! ')
                    game_on = False

                else:
                    turn = 'Player 2'
        else:
            # PLAYER 2 TURN
            # first we display the empty board
            display_board(the_board)

            # choose the position
            position = player_choice(the_board)

            # Place thw marker in the position
            place_marker(the_board, player2_marker, position)

            # check if placing it is a win
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Yoho!! Congratulations PLAYER 1 has WON ')
                game_on = False

            else:
                if check_boardfull(the_board):
                    display_board(the_board)
                    print('THE GAME HAS TIED !! ')
                    game_on = False

                else:
                    turn = 'Player 1'

    if replay() != True:
        break

# Break out of WHILE loop depending on replay() function
