#Juego de adivinar el numero para 2 personas

numero_usuario = input("Introduce el numero que se debera adivinar: ")
winner = False
numero_adivinar = input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nIntroduce el numero que creas que es: ")

while winner == False:
    if numero_usuario == numero_adivinar:
        print("Felicidades has ganado")
        winner = True
    else:
        print("Vuelve a intentarlo")
        winner = False
        numero_adivinar = input("Introduce denuevo el numero que creas que es: ")