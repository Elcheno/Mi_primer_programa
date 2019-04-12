#Ejercicio: programa para con tar los espacios, puntos, comas de una frase que alla introducido el usuario...

frase_usuario = input("Introduce una frase:  ")

mi_lista = [" ", ".", ",", "¿?", "!¡"]
lista_vocales = ["a", "e", "i", "o", "u"]
lista_mayusculas = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M",
                    "N", "Ñ", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
lista_vocales_mayusculas = ["A", "E", "I", "O", "U"]



espacios = 0
comas = 0
puntos = 0
vocal = 0
consonante = 0
interrogacion = 0
exclamacion = 0
vocales_mayusculas = 0
consonantes_mayusculas = 0



for letra in frase_usuario:
    if letra in lista_vocales:
        vocal += 1
    elif letra in mi_lista[0]:
        espacios += 1
    elif letra in mi_lista[1]:
        puntos += 1
    elif letra in mi_lista[2]:
        comas += 1
    elif letra in lista_vocales_mayusculas:
        vocales_mayusculas += 1
    elif letra in lista_mayusculas:
        consonantes_mayusculas += 1
    elif letra in mi_lista[3]:
        interrogacion += 1
    elif letra in mi_lista[4]:
        exclamacion += 1
    else:
        consonante += 1

print("Vocales: {}\nVocales Mayus.: {}\nConsonantes: {}\nConsonates Mayus.: {}\nEspacios: {}\nPuntos: {}\nComas: {}\n"
      "Interrogaciones: {}\nExclamaciones: {}".format(vocal, vocales_mayusculas, consonante, consonantes_mayusculas,
      espacios, puntos, comas, interrogacion, exclamacion))