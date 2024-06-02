from random import randrange

def display_board(board):
    # La función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola.
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ", board[0][0], "  |  ", board[0][1], "  |  ", board[0][2], "  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ", board[1][0], "  |  ", board[1][1], "  |  ", board[1][2], "  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ", board[2][0], "  |  ", board[2][1], "  |  ", board[2][2], "  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")

def enter_move(board):
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
    while True:
        movimiento = input("Ingresa tu movimiento (1-9): ")
        if movimiento not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print("Opción incorrecta")
            continue
        movimiento = int(movimiento) - 1
        row = movimiento // 3
        column = movimiento % 3
        if board[row][column] in ["X", "O"]:
            print("Casillero ocupado")
            continue
        board[row][column] = "O"
        break
    return board

def make_list_of_free_fields(board):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos.
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    list_of_free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['O', 'X']:
                list_of_free_fields.append((row, col))
    return list_of_free_fields

def victory_for(board, sign):
    # La función analiza el estatus del tablero para verificar si
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
    if board[0][0] == board[0][1] == board[0][2] == sign \
            or board[1][0] == board[1][1] == board[1][2] == sign \
            or board[2][0] == board[2][1] == board[2][2] == sign \
            or board[0][0] == board[1][0] == board[2][0] == sign \
            or board[0][1] == board[1][1] == board[2][1] == sign \
            or board[0][2] == board[1][2] == board[2][2] == sign \
            or board[0][0] == board[1][1] == board[2][2] == sign \
            or board[0][2] == board[1][1] == board[2][0] == sign:
        return True
    return False

def draw_move(board):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        random_select = randrange(len(free_fields))
        row, col = free_fields[random_select]
        board[row][col] = 'X'
    return board

def ask_play_again():
    while True:
        play_again = input("¿Jugar de nuevo? s/n: ")
        if play_again.lower() not in ["s", "n"]:
            print("Opción incorrecta")
            continue
        return play_again.lower() == "s"

# Flujo del juego
def main():
    while True:
        board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        board[1][1] = "X"
        winner = ""

        while True:
            display_board(board)
            board = enter_move(board)

            if victory_for(board, "O"):
                display_board(board)
                print("¡Ganaste!")
                break

            display_board(board)
            board = draw_move(board)

            if victory_for(board, "X"):
                display_board(board)
                print("¡Perdiste!")
                break

            if not make_list_of_free_fields(board):
                display_board(board)
                print("¡Empate!")
                break

        if not ask_play_again():
            print("¡Muchas gracias por jugar!")
            break

main()
