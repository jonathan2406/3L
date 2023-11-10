import pandas as pd
from tabulate import tabulate
from colorama import Fore, Style
import random

class Tablero:
    def __init__(self):
        self.matrix = [["-" for _ in range(4)] for _ in range(4)]

    def verificar(self, matrix): 
        for i in range(len(matrix)-1):
            for j in range(len(matrix)-1):
                if matrix[i][j] == "X" and matrix[i+1][j] == "X" and matrix[i+1][j+1] == "X":
                    return -1
                if matrix[i][j] == "O" and matrix[i+1][j] == "O" and matrix[i+1][j+1] == "O":
                    return 1
                
        if self.verificarEmpate(matrix) == True:
            return 0

    def verificarEmpate(self, matrix):
        for filas in matrix:
            for columnas in filas:
                if columnas == "-": return False
        return True
    
    def print(self, tablero):
        for i in tablero:
            print(i)

    def imprimirTablero(self):
        df = pd.DataFrame(self.matrix)
        df = df.replace({None: ' '})  
        df.index = [f"{Fore.BLUE}{i}{Style.RESET_ALL}" for i in df.index]
        df.columns = [f"{Fore.GREEN}{col}{Style.RESET_ALL}" for col in df.columns]
        print(tabulate(df, tablefmt="grid", headers="keys", showindex=True))

    def heuristica(self):
        for filas in range(len(self.matrix)-1):
            for columnas in range(len(self.matrix)):
                if self.vericarHeuristica(filas, columnas) == True:
                    return
        self.randomMax()

    def randomMax(self):
        while(True):
            filaRandom = random.randint(0,3)
            columnaRandom = random.randint(0,3)
            if self.matrix[filaRandom][columnaRandom] == '-':
                self.matrix[filaRandom][columnaRandom] = 'O'
                return
                    
                
    def vericarHeuristica(self, filas, columna):
        if self.matrix[filas][columna] == 'X':
            if self.matrix[filas+1][columna] == '-':
                self.matrix[filas+1][columna] = 'O'
                return True
        return False

    def minMax(self, tablero, turno, alfa=float('-inf'), beta=float('inf')):
        resultado = self.verificar(tablero)
        if resultado is not None:
            return resultado, None, []

        mejor_valor = float('-inf') if turno == 'O' else float('inf')
        mejor_jugada = None
        lista_hijos = []

        for filas in range(len(tablero)):
            for columnas in range(len(tablero[0])):
                if tablero[filas][columnas] == "-":
                    tablero[filas][columnas] = turno
                    valor, _, _ = self.minMax(tablero, 'X' if turno == 'O' else 'O', alfa, beta)
                    tablero[filas][columnas] = "-"

                    if turno == 'O':
                        if valor > mejor_valor:
                            mejor_valor = valor
                            mejor_jugada = (filas, columnas)
                        alfa = max(alfa, mejor_valor)
                    else:
                        if valor < mejor_valor:
                            mejor_valor = valor
                            mejor_jugada = (filas, columnas)
                        beta = min(beta, mejor_valor)

                    lista_hijos.append((valor, (filas, columnas)))

                    if alfa >= beta:
                        break  
        return mejor_valor, mejor_jugada, lista_hijos

    def encontrar_ganadora(self, lista_hijos):
        tablero_simulado = self.matrix
        for valor, coordenada in lista_hijos:
            if valor == 1:  
                tablero_simulado[coordenada[0]][coordenada[1]] = 'O'
                if self.verificar(tablero_simulado) == 1:  
                    return coordenada
        return False
    



