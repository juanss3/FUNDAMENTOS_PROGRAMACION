import random

# Configuración del tablero
board_size = 5
num_ships = 3
board = [["O"] * board_size for _ in range(board_size)]
ships = []

# Función para imprimir el tablero
def print_board(board):
    for row in board:
        print(" ".join(row))

# Colocar los barcos de forma aleatoria
def place_ships():
    while len(ships) < num_ships:
        ship_row = random.randint(0, board_size - 1)
        ship_col = random.randint(0, board_size - 1)
        if (ship_row, ship_col) not in ships:
            ships.append((ship_row, ship_col))

# Verificar el disparo del jugador
def check_guess(guess_row, guess_col):
    if (guess_row, guess_col) in ships:
        board[guess_row][guess_col] = "X"
        print("¡Le diste a un barco!")
        ships.remove((guess_row, guess_col))
        return True
    else:
        board[guess_row][guess_col] = "-"
        print("¡Fallaste!")
        return False

# Juego principal
def play_game():
    place_ships()
    print("¡Bienvenido a Batalla Naval!")
    print_board(board)

    turns = 0
    while len(ships) > 0:
        print(f"Turno {turns + 1}")
        guess_row = int(input("Adivina fila (0-4): "))
        guess_col = int(input("Adivina columna (0-4): "))

        if 0 <= guess_row < board_size and 0 <= guess_col < board_size:
            if check_guess(guess_row, guess_col):
                if len(ships) == 0:
                    print("¡Ganaste! Hundiste todos los barcos.")
                    break
            else:
                print("Intenta de nuevo.")
        else:
            print("Coordenadas fuera del tablero. Intenta de nuevo.")

        turns += 1
        print_board(board)

    if len(ships) > 0:
        print("¡Fin del juego! No hundiste todos los barcos.")

play_game()
