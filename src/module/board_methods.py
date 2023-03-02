from board_config import board_inicial, board_goal, BOARD_SIZE


def imprimir_tabuleiro(board):
    print("\n|++++++++++++++++++++++|")
    for linha in range(BOARD_SIZE):
        for coluna in range(BOARD_SIZE):

            if 0 < board[linha][coluna] < 10:
                print("| ", board[linha][coluna], "|", end="")

            if board[linha][coluna] >= 10:
                print("|", board[linha][coluna], "|", end="")

            if board[linha][coluna] == 0:
                print("| __ |", end="")
        print("\n|++++++++++++++++++++++|")
    print("\n")


def encontrar_vazio(board):
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == 0:
                return i, j


def generate_descendente(board):
    sucessores = []
    i, j = encontrar_vazio(board)
    if i > 0:
        copy_board = [row[:] for row in board]
        copy_board[i][j], copy_board[i - 1][j + 0] = copy_board[i - 1][j + 0], copy_board[i][j]
        sucessores.append(copy_board)
    if i < 3:
        copy_board = [row[:] for row in board]
        copy_board[i][j], copy_board[i + 1][j + 0] = copy_board[i + 1][j + 0], copy_board[i][j]
        sucessores.append(copy_board)
    if j > 0:
        copy_board = [row[:] for row in board]
        copy_board[i][j], copy_board[i + 0][j - 1] = copy_board[i + 0][j - 1], copy_board[i][j]
        sucessores.append(copy_board)
    if j < 3:
        copy_board = [row[:] for row in board]
        copy_board[i][j], copy_board[i + 0][j + 1] = copy_board[i + 0][j + 1], copy_board[i][j]
        sucessores.append(copy_board)
    return sucessores


def count_inversions(board):
    inversions = 0
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if board[i] > board[j] != 0 and board[i] != 0:
                inversions += 1
    return inversions


def is_solvable(board_i, board_f):
    inversions_i = count_inversions(board_i)
    inversions_f = count_inversions(board_f)
    solv_i = inversions_i % 2 == 0
    solv_f = inversions_f == 0
    if solv_i and solv_f:
        return True
    if (solv_i and not solv_f) or (not solv_i and solv_f):
        return False
    else:
        return True


# vê a legalidade de um movimento e executa esse movimento
def move_legalidade(board, x, y):
    i, j = encontrar_vazio(board)

    if (i + x < 0) or (i + x > 3) or (j + y < 0) or (j + y > 3):  # ilegalidades
        return False
    return True


def do_move(board, x, y):
    if move_legalidade(board, x, y):
        i, j = encontrar_vazio(board)
        board[i][j], board[i + x][j + y] = board[i + x][j + y], board[i][j]  # faz a jogada
        return board


# possíveis movimentos
def move_up(board):
    return do_move(board, -1, 0)


def move_right(board):
    return do_move(board, 0, 1)


def move_down(board):
    return do_move(board, 1, 0)


def move_left(board):
    return do_move(board, 0, -1)


def jogada(board, x):
    if x == "w" or x == 1:
        move_up(board)
    if x == "d" or x == 2:
        move_right(board)
    if x == "s" or x == 3:
        move_down(board)
    if x == "a" or x == 4:
        move_left(board)
    return board
