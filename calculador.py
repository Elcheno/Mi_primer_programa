#Calculadora

calculator = input("¿Que operacion quereis realizar: ?   (Multiplicacion / Division / Suma/ Resta)").upper()

operacion_uno = "MULTIPLICACION"
operacion_dos = "DIVISION"
operacion_tres = "SUMA"
operacion_cuatro = "RESTA"
numero_total = 0
numero_uno = 0
numero_dos = 0


numero_uno = int(input("Primer numero: "))
numero_dos = int(input("segundo numero: "))

if calculator == operacion_uno:
    numero_total = (numero_uno * numero_dos)
    print("El resultado de tu {} es {}".format(calculator, numero_total))
elif calculator == operacion_dos:
    numero_total = (numero_uno / numero_dos)
    print("El resultado de tu {} es {}".format(calculator, numero_total))
elif calculator == operacion_tres:
    numero_total = (numero_uno + numero_dos)
    print("El resultado de tu {} es {}".format(calculator, numero_total))
elif calculator == operacion_cuatro:
    numero_total = (numero_uno - numero_dos)
    print("El resultado de tu {} es {}".format(calculator, numero_total))