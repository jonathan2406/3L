import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

class Trapecio:

    def __init__(self, a=None, b=None, n=999):
        self.n = n
        self.f = None
        self.a = a
        self.b = b
        self.deltax = None
        self.lista_xi = []
        self.lista_funciones = []
        self.resultado = None
        self.x = sp.Symbol('x')

    def verificar_n(self):
        pass

    def generar_resultado(self):
        self.generar_diferencial()

        self.lista_funciones = [self.f.subs(sp.Symbol('x'), self.a + i * self.deltax) for i in range(self.n + 1)]

        self.resultado = ((self.deltax) / 2) * (self.lista_funciones[0] + 2 * sum(self.lista_funciones[1:-1]) + self.lista_funciones[-1])

    def generar_diferencial(self):
        self.deltax = (self.b - self.a) / self.n

    def set_f(self, funcion):
        self.f = sp.sympify(funcion)

    def get_f(self):
        return self.f

    def set_n(self, n):
        self.n = n

    def set_intervalo(self, a, b):
        self.a = a
        self.b = b

    def ver(self):
        print(f"""
        [-* Resultado Método del Trapecio *-]
        (Tipo {type(self)})
        -> ∫({self.f})dx
        n = {self.n}
        intervalo = [{self.a},{self.b}]
        Δx = {self.deltax}
        resultado = {self.resultado}
        """)

    def plot_funcion(self):
        if isinstance(self, Trapecio):
            x_vals = np.linspace(self.a, self.b, 1000)
            y_vals = [self.f.subs(sp.Symbol('x'), val) for val in x_vals]

            # Dividir el intervalo en n subintervalos
            subintervalos = np.linspace(self.a, self.b, self.n+1)

            # Pintar los trapecios
            for i in range(self.n):
                x_trapecio = [subintervalos[i], subintervalos[i], subintervalos[i+1], subintervalos[i+1], subintervalos[i]]
                y_trapecio = [0, self.f.subs(sp.Symbol('x'), subintervalos[i]), self.f.subs(sp.Symbol('x'), subintervalos[i+1]), 0, 0]
                plt.fill(x_trapecio, y_trapecio, 'b', alpha=0.5)

            plt.plot(x_vals, y_vals, label=f'f(x) = {self.f}')
            plt.xlabel('x')
            plt.ylabel('f(x)')
            plt.title('Gráfico de la Función con Trapecios')
            plt.legend()
            plt.show()




class Simpson13:

    def __init__(self, a=None, b=None, n=999):
        self.n = n
        self.f = None
        self.a = a
        self.b = b
        self.deltax = None
        self.lista_xi = []
        self.lista_funciones = []
        self.resultado = None
        self.x = sp.Symbol('x')

    def verificar_n(self):
        if self.n % 2 != 0:
            self.n += 1
            self.verificar_n()

    def generar_resultado(self):
        self.verificar_n()
        self.generar_diferencial()
        marcador = 4

        self.lista_funciones = [self.f.subs(sp.Symbol('x'), self.a + i * self.deltax) for i in range(self.n + 1)]

        for i in range(1, self.n):
            self.lista_funciones[i] *= 4 if marcador == 4 else 2
            marcador = 6 - marcador

        self.resultado = (1 / 3) * (self.deltax) * sum(self.lista_funciones)

    def generar_diferencial(self):
        self.deltax = (self.b - self.a) / self.n

    def set_f(self, funcion):
        self.f = sp.sympify(funcion)

    def get_f(self):
        return self.f

    def set_n(self, n):
        self.n = n

    def set_intervalo(self, a, b):
        self.a = a
        self.b = b

    def ver(self):
        print(f"""
        [-* Resultado Método de Simpson 1/3 *-]
        (Tipo {type(self)})
        -> ∫({self.f})dx
        n = {self.n}
        intervalo = [{self.a},{self.b}]
        Δx = {self.deltax}
        resultado = {self.resultado}
        """)

    def plot_funcion(self):
        x_vals = np.linspace(self.a, self.b, 1000)
        y_vals = [self.f.subs(sp.Symbol('x'), val) for val in x_vals]

        plt.plot(x_vals, y_vals, label=f'f(x) = {self.f}')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title('Gráfico de la Función')
        plt.legend()
        plt.show()


class Simpson38:

    def __init__(self, a=None, b=None, n=999):
        self.n = n
        self.f = None
        self.a = a
        self.b = b
        self.deltax = None
        self.lista_xi = []
        self.lista_funciones = []
        self.resultado = None
        self.x = sp.Symbol('x')

    def verificar_n(self):
        if self.n % 3 != 0:
            self.n += 1
            self.verificar_n()

    def generar_resultado(self):
        self.verificar_n()
        self.generar_diferencial()

        self.lista_funciones = [self.f.subs(sp.Symbol('x'), self.a + i * self.deltax) for i in range(self.n + 1)]

        for i in range(1, self.n):
            self.lista_funciones[i] *= 3 if i % 3 else 2

        self.resultado = (3 / 8) * self.deltax * sum(self.lista_funciones)

    def generar_diferencial(self):
        self.deltax = (self.b - self.a) / self.n

    def set_f(self, funcion):
        self.f = sp.sympify(funcion)

    def get_f(self):
        return self.f

    def set_n(self, n):
        self.n = n

    def set_intervalo(self, a, b):
        self.a = a
        self.b = b

    def ver(self):
        print(f"""
        [-* Resultado Método de Simpson 3/8 *-]
        (Tipo {type(self)})
        -> ∫({self.f})dx
        n = {self.n}
        intervalo = [{self.a},{self.b}]
        Δx = {self.deltax}
        resultado = {self.resultado}
        """)



x = sp.Symbol('x')

f1 = Trapecio(0, 3, 100)
f1.set_f((sp.E**x**2))
f1.generar_resultado()
f1.ver()
f1.plot_funcion()

