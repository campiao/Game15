from board_config import BOARD_SIZE


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


def imprimir_resultados(path, max_nodes, exe_time, num_moves):
    index = 1
    for board in path:
        if index == 1:
            print(f"Board inicial: {board}")
            index += 1
            continue
        print(f"Move {index - 1}: {board}")
        index += 1
    print("Numero maximo de nos em memoria: " + str(max_nodes))
    print("Tempo de execucao: " + str(exe_time))
    print("Numero de movimentos: " + str(num_moves))


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
    board_in_list = []
    for linha in board:
        for element in linha:
            board_in_list.append(element)
    inversions = 0
    for i in range(len(board_in_list) - 1):
        for j in range(i + 1, len(board_in_list)):
            if board_in_list[i] != 0 and board_in_list[j] != 0 and board_in_list[i] > board_in_list[j]:
                inversions += 1
    return inversions


def is_solvable(board):
    inversions = count_inversions(board)
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == 0:
                if (i % 2 != 0 and inversions % 2 == 0) or (i % 2 == 0 and inversions % 2 != 0):
                    return True
    return False


def final_position_reachable(board_i, board_f):
    return is_solvable(board_i) == is_solvable(board_f)


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
