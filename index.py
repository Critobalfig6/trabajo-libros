#libros
coleccion1 = []


def añadir_libro():
    titulo = input("ingresa el titulo del libro:")
    plataforma = input("ingresa la plataforma")
    
    try:
        año = int(input("ingresa el año: "))
    except ValueError:
        print("debes de colocar numeros enteros")
        return
    estado = input("ingrese el estado: ")

    libros = {
        "titulo": titulo,
        "plataforma" : plataforma,
        "año" : año,
        "estado" : estado,

    }
    coleccion1.append(libros)
    print("juego agregado perfectamente")

def listar_libros():
    if len(coleccion1) == 0:
        print("no se encuentra ningun libro")
        return
    
    for libros in coleccion1:

        print("--------------------")
        print("Título:", libros["titulo"])
        print("Plataforma:", libros["plataforma"])
        print("Año:", libros["año"])
        print("Estado:", libros["estado"])

def estadisticas():

    pendientes = 0

    for libros in coleccion1:
        if libros["estado"].lower() == "pendiente":
            pendientes += 1

    print("Juegos registrados:", len(coleccion1))
    print("Juegos pendientes:", pendientes)

def cambiar_estado():

    titulo = input("Ingrese el título del juego: ")

    encontrado = False

    for libros in coleccion1:

        if libros["titulo"].lower() == titulo.lower():

            print("Estado actual:", libros["estado"])

            nuevo_estado = input("Nuevo estado (pendiente/terminado): ")

            libros["estado"] = nuevo_estado

            print("Estado actualizado.")
            encontrado = True
            break

    if encontrado == False:
        print("Juego no encontrado.")