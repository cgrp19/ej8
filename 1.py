
class Conjunto:
    __conjunto = []

    def __init__(self):
        self.__conjunto = []

    def crearConjunto(self, tamaño):
        i = 0
        for i in range(int(tamaño)):
            self.__conjunto.append(input("Ingrese un numero: "))
    
    def nuevoConjunto(self, conjunto):
        self.__conjunto = conjunto

    def ordenar(self):
        self.__conjunto.sort()

    def mostrar(self):
        for num in self.__conjunto:
                print(num)


    def __add__(self, otro):
        otroconjunto = otro.__conjunto.copy()
        for numero in self.__conjunto:
            for otroNum in otro.__conjunto:
                if numero == otroNum:
                    numero_repetido = numero
                    otroconjunto.remove(numero_repetido)

        return self.__conjunto + otroconjunto
    
    def __sub__(self, otro):
        conjunto = self.__conjunto.copy()
        for numero in self.__conjunto:
            for otroNum in otro.__conjunto:
                if numero == otroNum:
                    numero_repetido = numero
                    conjunto.remove(numero_repetido)

        return conjunto
    
    def __eq__(self, otro):
        return self.__conjunto == otro.__conjunto