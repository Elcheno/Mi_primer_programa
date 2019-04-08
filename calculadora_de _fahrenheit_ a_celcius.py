#Calculadora de fahrenheits a celsius y al contrario...

celsius = 0
fahr = 0
fahr_usuario = 0
celcius_usuario = 0


print("Pon el tipo de operacion que quieres hacer")
tipo_operacion = input("(fahr-->celsius / celsius-->fahr): ")

if tipo_operacion == "fahr-->celsius":
    fahr_usuario = int(input("Pon el dato de temp. en fahrenheits: "))
    celsius = (fahr_usuario - 32) * 5 / 9
    print("{}ºF son {}ºC".format(fahr_usuario, celsius))
elif tipo_operacion == "celsius-->fahr":
    celsius_usuario = int(input("Pon el dato de temp. en celsius: "))
    fahr = (celsius_usuario * 9 / 5) + 32
    print("{}ºC son {}ºF".format(celsius_usuario, fahr))