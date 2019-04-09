
mi_lista = []
cantidad_compras = int(input("¿Cuantas cosas quieres comprar? \n(Cantidad exacta de productos a comprar):  "))
input_usuario = input("¿Que necesitas comprar?:  ").upper()

mi_lista.append(input_usuario)

while cantidad_compras != len(mi_lista):
    input_usuario = input("¿Que mas necesitas comprar?").upper()
    mi_lista.append(input_usuario)

print("\n\nEsta es la lista de la compra:\n")

for item in mi_lista:
    print("  Tengo que comprar {}".format(item))

print("\n\tFIN")