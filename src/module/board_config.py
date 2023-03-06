BOARD_SIZE = 4
board_inicial = []
board_goal = []


def read_inicial_n_final_state():
    def set_board(board):
        x = [int(num) for num in input("Introduzir board inicial e final, uma em cada linha: ").split()]
        for i in range(BOARD_SIZE):
            row = []
            for j in range(BOARD_SIZE):
                row.append(x[(i * 4) + j])
            board.append(row)
        print(board)

    set_board(board_inicial)
    set_board(board_goal)
