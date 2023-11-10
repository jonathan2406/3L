from Tablero import Tablero

class Game:
    def __init__(self) -> None:
        self.tablero = None
        self.turno = 0

    def run(self):
        print("Bienvenido a 3L")
        self.tablero = Tablero()
        self.tablero.matrix = [["-" for _ in range(4)] for _ in range(4)]
        while True:
            self.tablero.imprimirTablero()
            self.turnoMin()
            verificacion = self.tablero.verificar(self.tablero.matrix) 
            if verificacion == -1:
                print("Jugador X ganador...")
                self.tablero.imprimirTablero()
                return
            elif verificacion == 1:
                print("Jugador O ganador...")
                self.tablero.imprimirTablero()
                return
            elif verificacion == 0:
                print("Empate...")
                self.tablero.imprimirTablero()
                return
            self.tablero.imprimirTablero()
            self.turno += 1
            self.turnoMax()
            verificacion = self.tablero.verificar(self.tablero.matrix) 
            if verificacion == -1:
                print("Jugador X ganador...")
                self.tablero.imprimirTablero()
                return
            elif verificacion == 1:
                print("Jugador O ganador...")
                self.tablero.imprimirTablero()
                return
            elif verificacion == 0:
                print("Empate...")
                self.tablero.imprimirTablero()
                return
        
    def turnoMin(self):
        while True:
            try:
                fila = int(input("ingresa la fila: "))
                columna = int(input("ingresa la columna: "))
            except:
                print("ingresaste algo que no es un digito")
                continue
            if fila >= 4 or columna >= 4:
                print("numeros desproporcionados")
                continue
            elif self.tablero.matrix[fila][columna] != "-":
                print("ya hay algo hay")
                continue
            break
        self.tablero.matrix[fila][columna] = "X"

    def turnoMax(self):
        if self.turno <= 2:
            self.tablero.heuristica()
            return
        valor, coordenadaminiMax, listaHijos = self.tablero.minMax(self.tablero.matrix, 'O')
        comparacion = self.tablero.encontrar_ganadora(listaHijos)
        if comparacion == False:
            self.tablero.matrix[coordenadaminiMax[0]][coordenadaminiMax[1]] = 'O'
            return
        self.tablero.matrix[comparacion[0]][comparacion[1]] = 'O'
    
