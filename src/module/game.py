from random import randint, seed
from os import system
import copy
from queue import Queue

BOARD_SIZE = 4  # tamanho do tabuleiro
MAGNITUDE = 1000  # magnitude para baralhar o tabuleiro

# Tabuleiro inicial (placeholder):
board_inicial = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 0, 15]]

# Tabuleiro objetivo (placeholder):
board_goal = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]


# --------------------------------------------------------------------------

def set_board(board, tipo):
    if tipo == 1:
        prompt = "Introduz a board inicial: "
    else:
        prompt = "Introduz a board final: "
    x = [int(x) for x in input(prompt).split()]
    count = 0
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            board[i][j] = x[count]
            count += 1


# Função para imprimir o tabuleiro:
def imprimir_tabuleiro(board):
    print("\n|++++++++++++++++++++++|")
    for linha in range(BOARD_SIZE):
        for coluna in range(BOARD_SIZE):

            if (0 < board[linha][coluna] < 10):
                print("| ", board[linha][coluna], "|", end="")

            if (board[linha][coluna] >= 10):
                print("|", board[linha][coluna], "|", end="")

            if (board[linha][coluna] == 0):
                print("| __ |", end="")
        print("\n|++++++++++++++++++++++|")
    print("\n")



def count_inversions(board):
    inversions = 0
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if board[i] > board[j] != 0 and board[i] != 0:
                inversions += 1
    return inversions


def is_solvable(board):
    inversions = count_inversions(board)
    return inversions % 2 == 0


# retorna a posição do espaço vazio
def encontrar_vazio(board):
    for _x in range(BOARD_SIZE):
        for _y in range(BOARD_SIZE):
            if board[_x][_y] == 0:
                return _x, _y


# vê a legalidade de um movimento e executa esse movimento
def move_legalidade(board, x, y):
    _x, _y = encontrar_vazio(board)

    if (_x + x < 0) or (_x + x > 3) or (_y + y < 0) or (_y + y > 3):  # ilegalidades
        return False
    return True


def do_move(board, x, y):
    if (move_legalidade(board, x, y)):
        _x, _y = encontrar_vazio(board)
        board[_x][_y], board[_x + x][_y + y] = board[_x + x][_y + y], board[_x][_y]  # faz a jogada
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


# teste

# lê a jogada do jogador e executa
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


# descendentes
def descendente(board):
    sucessores = []
    _x, _y = encontrar_vazio(board)
    if _x > 0:
        copy_board = copy.deepcopy(board)
        copy_board[_x][_y], copy_board[_x - 1][_y + 0] = copy_board[_x - 1][_y + 0], copy_board[_x][_y]
        sucessores.append(copy_board)
    if _x < 3:
        copy_board = copy.deepcopy(board)
        copy_board[_x][_y], copy_board[_x + 1][_y + 0] = copy_board[_x + 1][_y + 0], copy_board[_x][_y]
        sucessores.append(copy_board)
    if _y > 0:
        copy_board = copy.deepcopy(board)
        copy_board[_x][_y], copy_board[_x + 0][_y - 1] = copy_board[_x + 0][_y - 1], copy_board[_x][_y]
        sucessores.append(copy_board)
    if _y < 3:
        copy_board = copy.deepcopy(board)
        copy_board[_x][_y], copy_board[_x + 0][_y + 1] = copy_board[_x + 0][_y + 1], copy_board[_x][_y]
        sucessores.append(copy_board)
    return sucessores


def heuristicadistancia(board):
    distancia = 0
    for i in range(4):
        for j in range(4):
            peca = board[i][j]
            if peca != 0:
                linha_objetivo = (peca - 1) // 4
                coluna_objetivo = (peca - 1) % 4
                distancia += abs(i - linha_objetivo) + abs(j - coluna_objetivo)
    return distancia


def heuristicalugar(board):
    n_errados = 0
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] != board_goal[i][j]:
                n_errados += 1
    return n_errados


# baralhar o tabuleiro
def shuffle(board):
    seed()
    for i in range(MAGNITUDE):
        m = randint(1, 4)
        jogada(board, m)

def bfs(board):
    queue=Queue()
    visited=set()
    queue.put(board,[])
    while not queue.empty():
        node,moves=queue.get()
        if node==board_goal: 
            return moves
        else: 
            if node not in visited:
                visited.add(node)
                next_moves=moves.copy()
                next_moves.append(descendente(board))
                for descendente in descendente(node):
                    if descendente not in visited:
                        queue.put(descendente)


def jogar(board, goal):
    set_board(board_inicial, 1)
    set_board(board_goal, 0)
    jogadas = 0
    print("\nO teu objetivo é chegar a esta configuração")
    imprimir_tabuleiro(goal)
    j = input("j para começar a jogar: ")
    if (j == 'j'):
        while (board != goal):
            system("clear")
            imprimir_tabuleiro(board)
            print("Número de jogadas: ", jogadas, "\n")
            print("w -> Cima\nd -> Direita\ns -> Baixo\na -> Esquerda\n \np -> Parar\n")
            x = input("Mover para: ")
            if (x == "p"):
                break
            if (jogada(board, x)):
                jogadas += 1  # como faço para não contar jogadas ilegais
                imprimir_tabuleiro(board)
        system("clear")
        imprimir_tabuleiro(board)
        print("Finalizaste o Puzzle\n")


jogar(board_inicial, board_goal)

print(descendente(board_inicial))
