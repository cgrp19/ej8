from ClaseConjunto import Conjunto

if __name__ == '__main__':
    n = input("Cantidad de numeros del conjunto: ")
    conjunto1 = Conjunto()
    conjunto1.crearConjunto(n)

    m = input("Cantidad de numeros del conjunto: ")
    conjunto2 = Conjunto()
    conjunto2.crearConjunto(m)

    ban = True
    while ban:
        print("Menu")
        print("1 - Suma")
        print("2 - Resta")
        print("3 - Igualdad")
        print("0 - Salir")
        op = input("Ingrese una opcion: ")

        if op == "1":
            conjuntosuma = Conjunto()
            suma = conjunto1 + conjunto2
            conjuntosuma.nuevoConjunto(suma)
            conjuntosuma.ordenar()
            conjuntosuma.mostrar()
            
        elif op == "2":
            conjuntoresta = Conjunto() 
            resta = conjunto1 - conjunto2
            conjuntoresta.nuevoConjunto(resta)
            conjuntoresta.ordenar()
            conjuntoresta.mostrar()
        
        elif op == "3":
            if conjunto1 == conjunto2:
                print("Los conjuntos son iguales")
            else:
                print("Los conjuntos no son iguales")


        elif op =="0":
            ban = False
        
        else:
            print("Opcion no valida")

