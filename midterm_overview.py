def slice_winner(slice):
    return slice == ['X', 'X', 'X'] or slice == ['O', 'O', 'O']


def row_winner(s):
    return slice_winner(s[:3]) or slice_winner(s[3:6]) or slice_winner(s[-3:])


def column_winner(s):
    return slice_winner(s[:9:3]) or slice_winner(s[1::3]) or slice_winner(s[2::3])


def diagonal_winner(s):
    return slice_winner(s[::4]) or slice_winner(s[2:7:2])


def check_winner(game_state):
    if row_winner(game_state) or column_winner(game_state) or diagonal_winner(game_state):
        return True
    else:
        return False


def print_field(li):
    for i in range(0, 7, 3):
        for j in range(0, 3):
            print(li[i + j], end=" ")
        print()


def reset_field():
    return [chr(ord('a') + x) for x in range(0, 10)]


def move_valid(game_state, pos):
    if not game_state[pos] == 'X' or not game_state[pos] == 'O':
        return True
    else:
        return False


li = [chr(ord('a') + x) for x in range(0, 10)]
game_active = True
valid_move = False
winner = False

while game_active:
    print_field(li)
    winner = False
    valid_move = False
    while not valid_move:
        print("Player 1 (X) Choose:")
        move = input().lower()
        for i in range(0, 10):
            if move == li[i]:
                if move_valid(li, i):
                    li[i] = 'X'
                    valid_move = True
                    break
            elif i == 9:
                print("Invalid Move, Pick again")
    valid_move = False
    if check_winner(li):
        print("X WINS! \n Play Again? (Y/N)")
        move = input().upper()
        while not valid_move:
            if move == 'Y':
                li = reset_field()
                winner = True
                valid_move = True
            elif move == 'N':
                exit()
    if not winner:
        print_field(li)
        while not valid_move:
            print("Player 2 (O) Choose:")
            move = input().lower()
            for i in range(0, 10):
                if move == li[i]:
                    if move_valid(li, i):
                        li[i] = 'O'
                        valid_move = True
                        break
                elif i == 9:
                    print("Invalid Move, Pick again")
        valid_move = False
        if check_winner(li):
            print("O WINS! \n Play Again? (Y/N)")
            move = input().upper()
            while not valid_move:
                if move == 'Y':
                    li = reset_field()
                    valid_move = True
                elif move == 'N':
                    exit()