# 1. Actualizar valores en diccionarios y listas

from typing import ItemsView
matriz = [ [10, 15, 20], [3, 7, 14] ]
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]


matriz[1][0] = 6                                     # Cambia 3 por 6 en matriz
cantantes[0]["nombre"] = "Enrique Martin Morales"    # Cambia nombre del primer cantante
ciudades["México"][2] = "Monterrey"                  # Cambia Cancún por Monterrey
coordenadas[0]["latitud"] = 9.9355431                # Cambia latitud

print(matriz)
print(cantantes)
print(ciudades)
print(coordenadas)

# 2. Iterar a través de una lista de diccionarios: imprime resultados en lineas separadas

def iterarDiccionario(lista): 
    for diccionario in lista:
        for llave, valor in diccionario.items():
            print(llave, "-", valor)

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

iterarDiccionario(cantantes)

# 2.1 BONUS: imprimir todo en una linea por cantante

def iterarDiccionario(lista):
    for diccionario in lista:
        linea = ""
        for llave, valor in diccionario.items():
            linea = linea + llave + " - " + valor + ", "
        print(linea)

iterarDiccionario(cantantes)


# 3. Obtener valores de una lista de diccionarios

def iterarDiccionario2(llave, lista):
    for diccionario in lista:
        valor = diccionario[llave]
        print(valor)


iterarDiccionario2("nombre", cantantes)
iterarDiccionario2("pais", cantantes)


# 4. Iterar a través de un diccionario con valores de lista

def imprimirInformacion(diccionario):
    for llave, lista in diccionario.items():
        print(len(lista), llave.upper())
        for valor in lista:
            print(valor)
        print()

costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

imprimirInformacion(costa_rica)


