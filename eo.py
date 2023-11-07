import abc
from typing import Any
import sympy as sp
import math

# Conocimientos sobre los procesos (Re algoritmicos xd):

# Método numérico del trapecio ->
# https://www.youtube.com/watch?si=3UzXNcNxCSbTrmEp&v=rREhW5wjkUI&feature=youtu.be

# Método numérico del Simpson 1/3 -> 
# https://www.youtube.com/watch?v=QCbGH6r3Hw0

class Integral(metaclass = abc.ABCMeta):

    def __init__(self, a = None, b = None, n = 999) -> None:
        self.n = n
        self.f = None
        self.a = a
        self.b = b
        self.deltax = None
        self.lista_xi = []
        self.lista_funciones = []
        self.resultado = None
        self.x = sp.Symbol('x')

    @abc.abstractmethod
    def verificar_n(self):
        pass

    def set_f(self, funcion):
        self.f = sp.sympify(funcion)
        
    def get_f(self):
        return self.f
    
    def set_n(self, n):
        self.n = n
    
    def set_intervalo(self, a, b):
        self.a = a
        self.b = b
    
    def generar_diferencial(self):
        self.deltax = (self.b - self.a) / self.n

    @abc.abstractmethod
    def generar_resultado(self):
        pass
        
    def __repr__(self):
        
        return f"""[-* Datos integral *-]
        (Tipo {type(self)})
        -> ∫({self.f})dx
        n = {self.n}
        intervalo = [{self.a},{self.b}]
        Δx = {self.deltax}
        resultado = {self.resultado}
        """
    
    def ver(self):
        print(self)

class Trapecio(Integral):

    def verificar_n(self):
        pass
    
    def generar_resultado(self):
        self.generar_diferencial()

        for i in range(self.n + 1):
            xi = self.a + (i * self.deltax)
            self.lista_xi.append(xi)
            fxi = self.f.subs(sp.Symbol('x'), xi)
            
            if (i in [0, self.n]):
                self.lista_funciones.append(fxi)
            
            else:
                self.lista_funciones.append(fxi*2)

        self.resultado = ((self.deltax) / 2) * sum(self.lista_funciones)

class Simpson13(Integral):

    def verificar_n(self):
        if self.n % 2 != 0:
            self.n += 1
            self.verificar_n()

    def generar_resultado(self):
        self.verificar_n()
        self.generar_diferencial()
        marcador = 4

        for i in range(self.n + 1):
            xi = self.a + (i * self.deltax)
            self.lista_xi.append(xi)
            fxi = self.f.subs(sp.Symbol('x'), xi)
            
            if (i in [0, self.n]):
                self.lista_funciones.append(fxi)
            
            elif (marcador == 4):
                self.lista_funciones.append(fxi*4)
                marcador = 2
            elif (marcador == 2):
                self.lista_funciones.append(fxi*2)
                marcador = 4

        self.resultado = (1/3) * (self.deltax) * sum(self.lista_funciones)

class Simpson38(Integral):

    # @override
    def verificar_n(self):
        if self.n % 3 != 0:
            self.n += 1
            self.verificar_n()

    def generar_resultado(self):
        self.verificar_n()
        self.generar_diferencial()

        for i in range(self.n + 1):
            xi = self.a + (i * self.deltax)
            fxi = self.f.subs(self.x, xi)

            if (i % 3 == 0):
                fxi *= 2

            else:
                fxi *= 3

            self.lista_xi.append(xi)
            self.lista_funciones.append(fxi)


        self.resultado = (3/8 ) * self.deltax * sum(self.lista_funciones)
        return self.resultado
    

x = sp.Symbol('x')

f1 = Simpson38(1, 4, 999)
f1.set_f((sp.E**x) * (sp.log(x, sp.E)))
f1.generar_resultado()
f1.ver()

f2 = Simpson13(1, 4, 12)
f2.set_f((sp.E**x) * (sp.log(x, sp.E)))
f2.generar_resultado()
f2.ver()

f3 = Trapecio(1, 4, 12)
f3.set_f((sp.E**x) * (sp.log(x, sp.E)))
f3.generar_resultado()
f3.ver()

