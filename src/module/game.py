from random import randint, seed
from os import system

board_size = 4 #tamanho do tabuleiro
MAGNITUDE = 1000 #magnitude para baralhar o tabuleiro
a
#Tabuleiro inicial:
board_inicial = [["|  1 |", "|  2 |", "|  3 |", "|  4 |"],
                 ["|  5 |", "|  6 |", "|  7 |", "|  8 |"],
                 ["|  9 |", "| 10 |", "| 11 |", "| __ |"],
                 ["| 13 |", "| 14 |", "| 15 |", "| 12 |"]]

#Tabuleiro objetivo:
board_goal = [["|  1 |", "|  2 |", "|  3 |", "|  4 |"],
              ["|  5 |", "|  6 |", "|  7 |", "|  8 |"],
              ["|  9 |", "| 10 |", "| 11 |", "| 12 |"],
              ["| 13 |", "| 14 |", "| 15 |", "| __ |"]]

#--------------------------------------------------------------------------


# Função para imprimir o tabuleiro:
def imprimir_tabuleiro(board):

    print("\n|++++++++++++++++++++++|")
    for linha in range(board_size):
        for coluna in range(board_size):
            print(board[linha][coluna],end="")
        print("\n|++++++++++++++++++++++|")
    print("\n")


def count_inversions(board):
    inversions = 0
    for i in range(len(board)):
        for j in range(i+1, len(board)):
            if board[i] > board[j] != 0 and board[i] != 0:
                inversions += 1
    return inversions

def is_solvable(board):
    inversions = count_inversions(board)
    return inversions % 2 == 0


#retorna a posição do espaço vazio
def encontrar_vazio(board):

    for _x in range(board_size):
        for _y in range(board_size):
            if board[_x][_y] == "| __ |":
                return _x, _y


#vê a legalidade de um movimento e executa esse movimento
def move(board,x,y):
    _x, _y = encontrar_vazio(board)

    if (_x + x < 0) or (_x + x > 3) or (_y + y < 0) or (_y + y > 3): #ilegalidades
        return False

    board[_x][_y], board[_x+x][_y+y] = board[_x+x][_y+y],board[_x][_y] #faz a jogada
    return True


#possíveis movimentos
def move_up(board):
    return move(board,-1, 0)

def move_right(board):
    return move(board,0, 1)

def move_down(board):
    return move(board,1, 0)

def move_left(board):
    return move(board,0, -1)


#lê a jogada do jogador e executa
def jogada(board,x):
    if x == "w" or x == 1:
        move_up(board)
    if x == "d" or x == 2:
        move_right(board)
    if x == "s" or x == 3:
        move_down(board)
    if x == "a" or x == 4:
        move_left(board)
    return board


#baralhar o tabuleiro
def shuffle(board):
    seed()
    for i in range(MAGNITUDE):
        m = randint(1,4)
        jogada(board,m)


def jogar(board,goal):
    jogadas = 0

    print("\nO teu objetivo é chegar a esta configuração")
    imprimir_tabuleiro(goal)
    j = input("j para começar a jogar: ")
    shuffle(board)
    if (j=='j'):
        while(board!=goal):
            system("clear")
            imprimir_tabuleiro(board)
            print("Número de jogadas: ", jogadas, "\n")
            print("w -> Cima\nd -> Direita\ns -> Baixo\na -> Esquerda\n \np -> Parar\n")
            x =input("Mover para: ")
            if(x == "p"):
                break

            if (jogada(board, x)):
                jogadas +=1 #como faço para não contar jogadas ilegais
                imprimir_tabuleiro(board)
        system("clear")
        imprimir_tabuleiro(board)
        print("Finalizaste o Puzzle\n")


jogar(board_inicial,board_goal)#