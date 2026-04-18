# 1. Imprime "Hola, mundo"
print( "Hola, Mundo")

# 2. Imprime "Hola, Valeria" con el nombre en una variable
nombre = "Juanjo"
print("Hola", nombre) # con una coma
print( "Hola " + nombre ) # con un +

# 3. Imprimir "Hola 9!" con el número en una variable
numero = 9
print( "Hola ", 9,"!" ) # con una coma
print( "Hola " + str(9),"!") # con un + -- este debería arrojar un error!, corrígelo con conversión

# 4. Imprimir "Me encanta comer tacos y arepas" con las comidas en variables
comida1 = "empanadas"
comida2 = "tallarines"
print("Me encanta comer {} y {} ".format(comida1, comida2)) # con .format()
print(f"Me encanta comer {comida1} y {comida2}") # con una cadena f

# 5. Bonus Ninja: adición

e = "empanadas"
t = "tallarines"
s = "Me gusta comer " + e + " y " + t 
print(s)

