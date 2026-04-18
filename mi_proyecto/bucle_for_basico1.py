
# 1. Básico: Imprime enteros de 0 a 100

for i in range(101):
    print(i)

# 2. Múltiples de 2: Imprime todos los multiples de 2 entre 2 y 500

for i in range(2, 501, 2):
    print(i)

# 3. Contando Vanilla Ice: n % x == 0 significa n es divisible por x 

for n in range(1, 101):
    if n % 10 == 0:
        print("baby")
    elif n % 5 == 0:
        print("ice ice")

# 4. WOW.Número gigante a la vista: operador +=, "suma y asignación"

total = 0
for i in range(0, 500001, 2):
    total += i
    print(total)


# 5. Regrésame al 3:

for n in range(2024, 0, -3):
    print(n)

# 6. Contador dinámico: 

numInicial = 1
numFinal = 27
multiplo = 3

for i in range(numInicial, numFinal + 1):
    if i % multiplo == 0:
        print(i)
