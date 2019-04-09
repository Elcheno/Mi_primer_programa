
apetece_helado = input("¿Te apetece un helado?  (Si/No):  ").upper()
if apetece_helado == "SI":
    dinero = input("¿Tines dinero para el helado?  (Si/No):  ").upper()
    if dinero == "SI":
        heladero_cerca = input("¿Esta el heladero cerca?(Si/No):  ").upper()
        if heladero_cerca == "SI":
            print("Genial, vamos a por el helado...")
        elif heladero_cerca == "NO":
            print("Valla que mala suerte...")
        else:
            print("No te he preguntado eso, pero supongo que no...")
    elif dinero == "NO":
        dinero_prestado = input("¿Quieres que te deje dinero para el helado?(Si/No):  ").upper()
        if dinero_prestado == "SI":
            heladero_cerca = input("¿Esta el heladero cerca?(Si/No):  ").upper()
            if heladero_cerca == "SI":
                print("Genial, vamos a por el helado...")
            elif heladero_cerca == "NO":
                print("Valla que mala suerte...")
            else:
                print("No te he preguntado eso, pero supongo que no...")
        elif dinero_prestado == "NO":
            print("Pues nada...")
        else:
            print("No te he preguntado eso, pero supongo que no...")
elif apetece_helado == "NO":
    print("Pues nada...")
else:
    print("No te he preguntado eso, pero supongo que no...")



















