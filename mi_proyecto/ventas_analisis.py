# Analisis de ventas: Utilizar listas, tuplas y diccionarios para realizar un análisis básico de datos de ventas utilizando Python.

# 1. Carga de datos: ventas de vegatales por fecha, producto, cantidad y precio.

ventas = [
    # Enero
    {"fecha": "2026-01-08", "producto": "Tomate", "cantidad": 8,  "precio": 900},
    {"fecha": "2026-01-15", "producto": "Papa",   "cantidad": 20, "precio": 450},
    {"fecha": "2026-01-22", "producto": "Palta",  "cantidad": 6,  "precio": 2100},
    # Febrero
    {"fecha": "2026-02-04", "producto": "Tomate", "cantidad": 10, "precio": 850},
    {"fecha": "2026-02-12", "producto": "Papa",   "cantidad": 18, "precio": 470},
    {"fecha": "2026-02-20", "producto": "Palta",  "cantidad": 4,  "precio": 1950},
    # Marzo
    {"fecha": "2026-03-06", "producto": "Tomate", "cantidad": 12, "precio": 950},
    {"fecha": "2026-03-14", "producto": "Papa",   "cantidad": 25, "precio": 430},
    {"fecha": "2026-03-21", "producto": "Palta",  "cantidad": 7,  "precio": 2200},
]

# 2. Cálculo de Ingresos Totales: cantidad vendida * precio_unitario*kilo

ingresos_totales = 0

for venta in ventas:
    ingresos_totales += venta["cantidad"] * venta["precio"]

print("Ingresos totales:", ingresos_totales)

# 3. Análisis del Producto Más Vendido:  crea diccionario llamado ventas_por_producto

ventas_por_producto = {}

for venta in ventas:
    producto = venta["producto"]
    if producto not in ventas_por_producto:  # para el caso de que agreguemos un nuevo producto que no esta en el diccionario.
        ventas_por_producto[producto] = 0
    ventas_por_producto[producto] += venta["cantidad"]

print(ventas_por_producto)

# 3.1 identifica el producto que tuvo la mayor cantidad total vendida.

producto_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)

print("Producto más vendido:", producto_mas_vendido)
print("Cantidad total:", ventas_por_producto[producto_mas_vendido])


# 4.Promedio de Precio por Producto:


precios_por_producto = {} # Diccionario vacío que irá guardando (suma_ingresos, cantidad_total) por producto

for venta in ventas:
    producto = venta["producto"]
    
    if producto not in precios_por_producto:    # Si el producto no existe aún, usamos una tupla (0, 0)

        precios_por_producto[producto] = (0, 0)
    
    suma, cantidad = precios_por_producto[producto]
    
    precios_por_producto[producto] = (suma + venta["precio"] * venta["cantidad"], cantidad + venta["cantidad"])

print(precios_por_producto)

for producto, (suma, cantidad) in precios_por_producto.items():
    promedio = suma / cantidad
    print(producto, ": precio promedio = ", round(promedio))


# 5. Ventas por Día: #similar al paso 3 solo que agrupa por fecha

ingresos_por_dia = {}

for venta in ventas:
    fecha = venta["fecha"]
    if fecha not in ingresos_por_dia:
        ingresos_por_dia[fecha] = 0
    ingresos_por_dia[fecha] += venta["cantidad"] * venta["precio"]

for fecha, ingreso in ingresos_por_dia.items():
    print(fecha, ": ", ingreso)

# print(ingresos_por_dia) # para verificar si se escribio correctamente el diccionario.


# 6. Representación de Datos

resumen_ventas = {}

for producto in ventas_por_producto:
    suma, cantidad = precios_por_producto[producto]
    resumen_ventas[producto] = {
        "cantidad_total": ventas_por_producto[producto],
        "ingresos_totales": suma,
        "precio_promedio": round(suma / cantidad)
    }

for producto, datos in resumen_ventas.items():
    print(producto, ":", datos)

# 7. script para crear resultados en un archivo de texto
with open("/home/kuku/Sonda-data/b2b-sonda-ds-2026/mi_proyecto/resultados_ventas.txt", "w") as f:

    # 1. Lista de ventas original
    f.write("PASO 1: LISTA DE VENTAS ORIGINAL\n")
    f.write("=" * 40 + "\n")
    f.write("Se cargaron 9 ventas correspondientes a 3 productos\n")
    f.write("(Tomate, Papa, Palta) durante los meses de enero,\n")
    f.write("febrero y marzo de 2026. Precios referenciales ODEPA.\n\n")
    for venta in ventas:
        f.write(str(venta) + "\n")

    # 2. Ingresos totales
    f.write("\nPASO 2: INGRESOS TOTALES\n")
    f.write("=" * 40 + "\n")
    f.write("Se iteró sobre cada venta multiplicando cantidad x precio.\n")
    f.write("Los resultados se acumularon en una variable suma.\n\n")
    f.write("Total generado: $" + str(ingresos_totales) + "\n")

    # 3. Producto más vendido
    f.write("\nPASO 3: PRODUCTO MAS VENDIDO\n")
    f.write("=" * 40 + "\n")
    f.write("Se construyó un diccionario con la cantidad total\n")
    f.write("vendida por producto sumando todas sus ventas.\n\n")
    for producto, cantidad in ventas_por_producto.items():
        f.write(producto + ": " + str(cantidad) + " kg\n")
    f.write("\nProducto mas vendido: " + producto_mas_vendido + " con " + str(ventas_por_producto[producto_mas_vendido]) + " kg\n")

    # 4. Precio promedio
    f.write("\nPASO 4: PRECIO PROMEDIO POR PRODUCTO\n")
    f.write("=" * 40 + "\n")
    f.write("Se usaron tuplas para guardar (suma_ingresos, cantidad)\n")
    f.write("por producto. El promedio se calculó como suma / cantidad.\n\n")
    for producto, (suma, cantidad) in precios_por_producto.items():
        f.write(producto + ": $" + str(round(suma / cantidad)) + " por kg\n")

    # 5. Ingresos por día
    f.write("\nPASO 5: INGRESOS POR DIA\n")
    f.write("=" * 40 + "\n")
    f.write("Se acumularon los ingresos agrupando por fecha.\n\n")
    for fecha, ingreso in ingresos_por_dia.items():
        f.write(fecha + ": $" + str(ingreso) + "\n")

    # 6. Resumen
    f.write("\nPASO 6: RESUMEN DE VENTAS POR PRODUCTO\n")
    f.write("=" * 40 + "\n")
    f.write("Se consolidaron cantidad total, ingresos y precio\n")
    f.write("promedio en un diccionario anidado por producto.\n\n")
    for producto, datos in resumen_ventas.items():
        f.write(producto + ":\n")
        f.write("  Cantidad total: " + str(datos["cantidad_total"]) + " kg\n")
        f.write("  Ingresos totales: $" + str(datos["ingresos_totales"]) + "\n")
        f.write("  Precio promedio: $" + str(datos["precio_promedio"]) + "\n")

print("Archivo generado: resultados_ventas.txt")