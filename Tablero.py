import pandas as pd
from tabulate import tabulate
from colorama import Fore, Style
import time

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

    def minMax(self, tablero, turno):
        resultado = self.verificar(tablero)
        if resultado is not None:
            return resultado, None

        if turno == 'O':
            mejor_valor = float('-inf')
        else:
            mejor_valor = float('inf')

        mejor_jugada = None

        for filas in range(len(tablero)):
            for columnas in range(len(tablero[0])):
                if tablero[filas][columnas] == "-":
                    tablero[filas][columnas] = turno
                    valor, _ = self.minMax(tablero, 'X' if turno == 'O' else 'O')
                    tablero[filas][columnas] = "-"

                    if turno == 'O':
                        if valor > mejor_valor:
                            mejor_valor = valor
                            mejor_jugada = (filas, columnas)
                    else:
                        if valor < mejor_valor:
                            mejor_valor = valor
                            mejor_jugada = (filas, columnas)

        return mejor_valor, mejor_jugada

        
eo = Tablero()
eo.matrix = [["X","O","-",'-'],
             ["O","O","-",'-'],
             ["X","-","-",'-'],
             ['X','O','X','O']]

matriz = eo.minMax(eo.matrix, "O")
print(matriz)






        



