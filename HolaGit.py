from io import open # Manejo de archivos

def leerArchivo():
    try:
        # Puntero al archivo
        archivo = open("datosAFD.txt", "r")

        # Leer las lineas y guardarlas en una lista
        texto = archivo.readlines()

        # Obtenemos los datos enteros y los almacenamos en una lista
        for t in texto[0]:
            if t.isdigit():
                estados.append(int(t))

        for t in texto[1]:
            if t.isdigit():
                qActual = int(t)

        for t in texto[2]:
            if t.isdigit():
                qFinales.append(int(t))

        for t in texto[3]:
            if ord(t) >= ord('a') and ord(t) <= ord('z'):
                alfabeto.append(t)

        llenarTransiciones(texto[4])

        print(f'Estados: {estados}')
        print(f'qActual: {qActual}')
        print(f'qFinales: {qFinales}')
        print(f'Alfabeto: {alfabeto}')
        print(f'Transiciones: {transiciones}')
    except FileNotFoundError:
        print("El archivo no fue encontrado")
    finally:
        archivo.close()

def llenarTransiciones(lista):
    # Partición para obtener las filas y analizarlas
    listaAux = lista.split(']')

    for dato in listaAux:
        # Almacena listas pequeñas (filas)
        listaAux2 = []

        for c in dato:
            if c.isdigit():
                listaAux2.append(int(c))
        
        if len(listaAux2):
            transiciones.append(listaAux2)
            #listaAux2.clear()

cadena = ""                             # string a procesar
estados = []                            # estados = filas
alfabeto = []                           # alfabeto = columnas
transiciones = []                       # tabla de transiciones - [FILAS][COLUMNAS]
qActual = 0                             # estado en el que se encuentra
qFinales = []                           # alamacena todos los estados finales
banderaAceptacion = False

leerArchivo()
print("\n")

while(True):
    cadena = input("Ingrese una cadena: ")

    # Para romper el ciclo infinito
    if cadena.lower() == "salir":
        break

    # Se obtiene caracter a caracter
    for c in cadena:
        if c == 'a' or c == 'b':
            # ord() convierte un caracter a entero y chr() lo contrario
            qActual = transiciones[qActual][ord(c)-ord('a')]

    # Se obtienen los estados finales uno a uno
    for final in qFinales:
        if qActual == final:
            banderaAceptacion = True
            break

    if banderaAceptacion == True:
        print("La cadena: " + cadena + " SI pertenece al lenguaje\n")
    else:
        print("La cadena: " + cadena + " NO pertenece al lenguaje\n")

    # Se cambian sus valores para no comenzar de cero la siguiente iteracións
    banderaAceptacion = False
    qActual = 0

print("Ejecucón finalizada")
