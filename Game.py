from Tablero import Tablero

class Game:
    def __init__(self) -> None:
        self.tablero = None

    def run(self):
        print("Bienvenido a 3L")
        self.tablero = Tablero()
        while True:
            self.tablero.imprimirTablero()
            self.turnoMin()
            verificacion = self.tablero.verificar(self.tablero.matrix) 
            if verificacion == -1:
                print("Jugador X ganador...")
                return
            elif verificacion == 1:
                print("Jugador O ganador...")
                return
            elif verificacion == 0:
                print("Empate...")
                return
            posicion = self.tablero.minMax(self.tablero.matrix, 'O')[1]
            self.tablero.matrix[posicion[0]][posicion[1]] = 'O'
        
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
    

 

eo = Game()
eo.run()