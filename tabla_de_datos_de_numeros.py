#Ejercicio 1: Programa que te pida diez numeros y los compare para identificar el mas pequeño...

#Ejericicio 2: Crea un programa que cuente los elementos de la lista de números introducida por el usuario**
#**Está prohibido utilizar la función len() para resolver el problema...

#Ejercicio 3: Crea un programa que calcule la media de los elementos de la lista de números introducida por el usuario...

numeros_usuario = []
numero_principal = ""

numero_de_numeros = int(input("¿Cuantos numeros quieres comprobar?: "))

while len(numeros_usuario) < numero_de_numeros:
    numero_principal = input("Dime un numero: ")
    while not numero_principal.isdigit():
        numero_principal = input("Esto no es numero: ")
    int(numero_principal)
    numeros_usuario.append(int(numero_principal))
    numero_principal = ""
    print("¡Numero añadido!")

numero_grande = numeros_usuario[0]
numero_pequeno = numeros_usuario[0]
suma_de_los_numeros = 0
numero_two = 0
media_total = 0

for numero in numeros_usuario:
    if numero_grande < numero:
        numero_grande = numero

print("\nEl numero mas grande es: {}".format(numero_grande))

for numero in numeros_usuario:
    if numero_pequeno > numero:
        numero_pequeno = numero

print("El numero mas pequeño es: {}".format(numero_pequeno))

for numero in  numeros_usuario:
    suma_de_los_numeros = numero + numero_two
    numero_two = suma_de_los_numeros

print("La suma total de los numeros es: {}".format(suma_de_los_numeros))

media_total = suma_de_los_numeros / numero_de_numeros

print("La media total es: {}".format(media_total))
print("Lista numeros: {}".format(numeros_usuario))
print("Numeros totales: {}".format(numero_de_numeros))