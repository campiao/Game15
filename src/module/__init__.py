from game import argv, jogar_player, jogar_ai

if __name__ == '__main__':
    try:
        len(argv[1])
    except:
        jogar_player()
    else:
        jogar_ai()
