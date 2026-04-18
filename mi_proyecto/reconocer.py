'''
Tarea: Reconocer Python
Objetivo: Identificar conceptos de programación en el código.
Nombre: Juan José Arellano
'''

numero1 = 70 # Declaración de variable. Inicializar número entero (integer)
numero2 = 3.14 # Declaración de variable. Inicializar número decimal (float)
booleano = False # Declaración de variable. Inicializar dato primitivo boolean 
cadena = 'Hola Mundo' # Declaración de variable. Inicializar dato primitivo, string
ingredientes_pastel = ['Harina', 'Leche', 'Huevos', 'Vainilla', 'Chocolate'] # Declaración de variable. Inicializacion de datos cumpuestos, lista.
persona = {'nombre': 'Patricio', 'pais': 'México', 'edad': 35, 'soltero': False} # Declaración de variable. Incialización de datos compuestos, diccionario.
frutas = ('guayaba', 'fresa', 'papaya') # Declaracion de variable. Incialización de datos compuestos, tupla.
print(type(frutas)) # Revisión de tipo, datos compuestos, tupla.
print(ingredientes_pastel[2]) # Datos compuestos, listas, accesar valor.
ingredientes_pastel.append('Mantequilla') # Datos compuestos, listas, agregar valor.
print(persona['nombre']) # Datos compuestos, diccionario, accesar valor. 
persona['nombre'] = 'Kevin' # Datos compuestos, diccionario, cambiar valor.
persona['color_ojos'] = 'cafe' # Datos compuestos, diccionario, agregar valor.
print(frutas[2]) # Datos compuestos, tupla, accesar valor 2 = fresa.

if numero1 > 45: # Condicional, if.
    print("Numero mayor")
else: # Condicional, else						
    print("Numero menor")

if len(cadena) < 5: # Condicional, if. Revisión de tamaño.
    print("Cadena corta")
elif len(cadena) > 15: # Condicinal, else if. Revisión de tamaño.
    print("Cadena larga")
else: # Condicional else.
    print("Cadena perfecta")

for x in range(8): # Bucle for, inicio.
    print(x)
for x in range(2,8): # Bucle for, inicio, fin.
    print(x)
for x in range(2,8,2): # Bucle for, inicio, fin, incremento.
    print(x)
x = 0		# Declaracion de vairable, dato primitivo numeral. 
while(x < 8): # Bucle while, inicio, fin
    print(x)
    x += 1 # Bucle while, incremento.

ingredientes_pastel.pop() # Datos compuestos, listas, borrar valor
ingredientes_pastel.pop(1) # Datos compuestos, listas, borra valor (en la segunda posición).

print(persona) # Datos compuestos, diccionario, accesar valor.
persona.pop('color_ojos') # Datos compuestos, diccionarios, borrar valor.
print(persona) # Datos compuestos, diccionarios, accesar valor.

for ingrediente in ingredientes_pastel: # Bucle for
    if ingrediente == 'Harina': # condicional, if
        continue # Bucle for, continue
    print('Después de la primera sentencia') 
    if ingrediente == 'Chocolate': # Condicional, if
        break	# Bucle for, break.

def imprime_hola_10_veces(): # Función
    for numero in range(10): # Bucle for, fin.
        print('Hola')

imprime_hola_10_veces() # Función

def imprime_hola_n_veces(n): # Función, parámetro
    for numero in range(n): # Bucle for, fin
        print('Hola')

imprime_hola_n_veces(5) # Función, argumento

def imprime_hola_n_o_diez_veces(n = 10): # Función, parámetro, 
    for numero in range(n): # Bucle for, fin
        print('Hola')

imprime_hola_n_o_diez_veces() # Función
imprime_hola_n_o_diez_veces(5) # Función, argumento.


"""
Sección BONUS
"""

# print(numero3) # NameError
# numero3 = 86 # Declaracion de variable, dato primitivo, numeral.
# frutas[0] = 'naranja' # TypeError
# print(persona['hobbies']) # KeyError
# print(ingredientes_pastel[11]) # IndexError
#   print(booleano) # IndentationError
# frutas.append('manzana') # AtributeError
# frutas.pop(1) # AtributeError
