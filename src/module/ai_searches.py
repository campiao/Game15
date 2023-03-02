from collections import deque
from board_methods import *
from time import time


def bfs():
    max_nodes = 0
    start_time = time()
    queue = deque()
    queue.appendleft([board_inicial])
    visited = set()
    while queue:
        max_nodes = max(max_nodes, len(queue))
        path = queue.pop()
        node = path[-1]
        if node == board_goal:
            end_time = time()
            return path, end_time - start_time, max_nodes
        if str(node) in visited:
            continue
        visited.add(str(node))
        for succesor in generate_descendente(node):
            new_path = path + [succesor]
            queue.appendleft(new_path)
    return None


def dfs():
    max_nodes = 0
    start_time = time()
    stack = [[board_inicial]]
    visited = set()
    while stack:
        max_nodes = max(max_nodes, len(stack))
        path = stack.pop()
        node = path[-1]
        if node == board_goal:
            end_time = time()
            return path, end_time - start_time, max_nodes
        if str(node) in visited:
            continue
        visited.add(str(node))
        for succesor in generate_descendente(node):
            new_path = path + [succesor]
            stack.append(new_path)
    return None


def a_star(heuristic):
    return None


def greedy(board):
    return None


def iterativo(board):
    return None


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
