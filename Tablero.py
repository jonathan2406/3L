import pandas as pd
from tabulate import tabulate
from colorama import Fore, Style
import time

class Tablero:
    def __init__(self):
        self.matrix = [["-" for _ in range(4)] for _ in range(4)]

    def verificar(self): 
        for i in range(len(self.matrix)-1):
            if self.matrix[i][i] == "X" and self.matrix[i+1][i] == "X" and self.matrix[i+1][i+1] == "X":
                return -1
            elif self.matrix[i][i] == "O" and self.matrix[i+1][i] == "O" and self.matrix[i+1][i+1] == "O":
                return 1
            elif self.verificarEmpate() == True:
                return 0

    def verificarEmpate(self):
        for filas in self.matrix:
            for columnas in filas:
                if columnas == "-": return False
        return True
    
    def print(self, tablero):
        print(tablero)

    def imprimirTablero(self):
        df = pd.DataFrame(self.matrix)
        df = df.replace({None: ' '})  
        df.index = [f"{Fore.BLUE}{i}{Style.RESET_ALL}" for i in df.index]
        df.columns = [f"{Fore.GREEN}{col}{Style.RESET_ALL}" for col in df.columns]
        print(tabulate(df, tablefmt="grid", headers="keys", showindex=True))

    #hasta aqui se lleva un avance considerable con el minimax
    def minMax(self,tablero, turno):
        resultado = self.verificar()
        print(self.print(tablero))
        if resultado is not None:
            return resultado

        if turno == 'O':
            mejor_valor = -1 
        else:
            mejor_valor = 1 

        for filas in range(len(tablero)):
            for columnas in range(len(tablero[0])):
                if tablero[filas][columnas] == "-":
                    tablero[filas][columnas] = turno
                    valor = self.minMax(tablero, 'X' if turno == 'O' else 'O')
                    tablero[filas][columnas] = "-"

                    if turno == 'O':
                        mejor_valor = max(mejor_valor, valor)
                    else:
                        mejor_valor = min(mejor_valor, valor)

        return mejor_valor

        



eo = Tablero()
eo.matrix[0][0] = "X"
matriz = eo.dfs_evaluacion(eo.matrix, "O")
print(matriz)


        



