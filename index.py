coleccion1 = []

def añadir_juego():
    titulo = input("ingresa el titulo del juego:")
    plataforma = input("ingresa la plataforma")
    
    try:
        año = int(input("ingresa el año: "))
    except ValueError:
        print("debes de colocar numeros enteros")
        return