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
		if movimiento not in ["1","2","3","4","5","6","7","8","9"]:
			print("Opción incorrecta")
			continue
		movimiento = int(movimiento) - 1
		row = movimiento // 3
		column = movimiento % 3
		if board[row][column] in ["X","O"]:
			print("Casillero ocupado")
			continue
		board[row][column] = "O"
		break


def make_list_of_free_fields(board):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos.
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    list_of_free_fields = []
    for row in range(3):
        for col in range(3): 
            if board[row][col] not in ['O','X']:
                list_of_free_fields.append((row,col)) 
    return list_of_free_fields


def victory_for(board, sign):
    # La función analiza el estatus del tablero para verificar si
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
    global winner
    if board[0][0] == board[0][1] == board[0][2] == sign\
    or board[1][0] == board[1][1] == board[1][2] == sign\
    or board[2][0] == board[2][1] == board[2][2] == sign\
    or board[0][0] == board[1][0] == board[2][0] == sign\
    or board[0][1] == board[1][1] == board[2][1] == sign\
    or board[0][2] == board[1][2] == board[2][2] == sign\
    or board[0][0] == board[1][1] == board[2][2] == sign\
    or board[0][2] == board[1][1] == board[2][0] == sign:
         winner = sign         


def draw_move(board):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.
    casillas_libres = make_list_of_free_fields(board)
    cantidad_de_libres = len(casillas_libres)
    if cantidad_de_libres > 0:	
        seleccion_aleatoria = randrange(cantidad_de_libres)
        row, col = casillas_libres[seleccion_aleatoria]
        board[row][col] = 'X'



# Flujo del juego
board = [[1,2,3],[4,5,6],[7,8,9]]
board[1][1] = "X"
winner = ""

while True:
    display_board(board)
    enter_move(board)
    
    victory_for(board, "O")
    victory_for(board, "X")
    if winner == "X":
        display_board(board)
        print("¡Perdiste!")
        break
    if winner == "O":
        display_board(board)
        print("¡Ganaste!")
        break
   
    display_board(board)   
    draw_move(board)

    victory_for(board, "O")
    victory_for(board, "X")
    if winner == "X":
        display_board(board)
        print("¡Perdiste!")
        break
    if winner == "O":
        display_board(board)
        print("¡Ganaste!")
        break
    if len(make_list_of_free_fields(board)) == 0:
        display_board(board)
        print("¡Empate!")
        break
         
    
        

    