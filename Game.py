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
            verificacion = self.tablero.verificar() 
            if verificacion == -1:
                print("Jugador X ganador...")
                return
            elif verificacion == 1:
                print("Jugador O ganador...")
                return
            elif verificacion == 0:
                print("Empate...")
                return
        
    def turnoMin(self):
        while True:
            fila = input("ingresa la fila: ")
            columna = input("ingresa la columna: ")
            if fila.isdigit() == False or columna.isdigit() == False:
                print("ingresaste algo que no es un digito")
                continue
            elif fila >= 4 or columna >= 4:
                print("numeros desproporcionados")
                continue
            elif self.tablero.matrix[fila][columna] != "-":
                print("ya hay algo hay")
                continue
            break
        self.tablero.matrix[fila][columna] = "X"
    

 

