# 1. función multiplica_por_dos(num)

def multiplica_por_dos(num):
    lista = []
    for i in range(num + 1):
        lista.append(i * 2)
    return lista

print(multiplica_por_dos(10))

# 2.  función suma_y_resta(lista)

def suma_y_resta(lista):
    print(lista[0] + lista[1])
    return lista[0] - lista[1]

print(suma_y_resta([5,4]))

# 3. función suma_y_resta(lista)

def sumatoria_menos_longitud(lista):
    return sum(lista) - len(lista)

print(sumatoria_menos_longitud([1, 2, 3, 4]))


# 4. Valores multiplicados por el segundo

def valores_multiplicados_segundo(lista):
    if len(lista) < 2:
        return []
    print(len(lista))
    nueva_lista = [n * lista[1] for n in lista]
    return nueva_lista

print(valores_multiplicados_segundo([1, 3, 5, 7]))
print(valores_multiplicados_segundo([1]))

# 5. Valor multiplado y longitud

def valor_multiplicado_longitud(valor, longitud):
    return [longitud * valor] * longitud

print(valor_multiplicado_longitud(5, 2))
print(valor_multiplicado_longitud(7, 5))
