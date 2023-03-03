from sys import argv
from os import system

from board_config import *
from ai_searches import bfs, dfs, a_star, greedy, iterativo, heuristicalugar, heuristicadistancia
from board_methods import *


# --------------------------------------------------------------------------


def jogar_player():
    read_inicial_n_final_state()
    jogadas = 0
    board_atual = board_inicial
    if not is_solvable(board_inicial, board_goal):
        print("Esta configuração não tem solução...")
        return
    print("\nO objetivo é chegar a esta configuração")
    imprimir_tabuleiro(board_goal)
    j = input("j para começar a jogar: ")
    if j == 'j':
        while board_atual != board_goal:
            system("clear")
            imprimir_tabuleiro(board_atual)
            print("Número de jogadas: ", jogadas, "\n")
            print("w -> Cima\nd -> Direita\ns -> Baixo\na -> Esquerda\n \np -> Parar\n")
            x = input("Mover para: ")
            if x == "p":
                break
            if jogada(board_atual, x):
                jogadas += 1  # como faço para não contar jogadas ilegais
                imprimir_tabuleiro(board_atual)
            system("clear")
            imprimir_tabuleiro(board_atual)
    print("Finalizaste o Puzzle\n")


def jogar_ai():
    read_inicial_n_final_state()
    ai_search = argv[1]
    print(ai_search)
    if ai_search == 'BFS':
        path, time_elapsed, max_nodes = bfs()
        print(path, len(path) - 1, time_elapsed, max_nodes)
    elif ai_search == 'DFS':
        path, time_elapsed, max_nodes = dfs()
        print(path, len(path) - 1, time_elapsed)
    elif ai_search == "Greedy-misplaced":
        path, time_elapsed, max_nodes = greedy(heuristicalugar)
        for board in path:
            imprimir_tabuleiro(board)
        print(len(path) - 1, time_elapsed, max_nodes)
    elif ai_search == "Greedy-Manhattan":
        path, time_elapsed, max_nodes = greedy(heuristicadistancia)
        for board in path:
            imprimir_tabuleiro(board)
        print(len(path) - 1, time_elapsed, max_nodes)
    elif ai_search == 'A*-misplaced':
        path, time_elapsed, max_nodes = a_star(heuristicalugar)
        for board in path:
            imprimir_tabuleiro(board)
        print(len(path) - 1, time_elapsed, max_nodes)
    elif ai_search == 'A*-Manhattan':
        path, time_elapsed, max_nodes = a_star(heuristicadistancia)
        for board in path:
            imprimir_tabuleiro(board)
        print(len(path) - 1, time_elapsed, max_nodes)
