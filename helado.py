apetece_helado_input = input("¿Te apetece un helado?  (si / no)").upper()

if apetece_helado_input == "SI":
    apetece_helado = True
elif apetece_helado_input == "NO":
    apetece_helado_input = False
else:
    print("Te he preguntado que si querias un helado lo demas no me interesa, ya imagino que no")
    apetece_helado_input = False

dinero_input = input("¿Tienes dinero para el helado?  (si / no)").upper()
tia_input = input ("¿Estas con tia?  (si / no)").upper()
heladero_input = input("¿Esta el heladero cerca?  (si / no)").upper()


dinero = dinero_input == "SI"
tia = tia_input == "SI"
permitirselo = dinero or tia
heladero = heladero_input == "SI"

if apetece_helado or permitirselo or heladero:
    print("¡Pues comete el puto helado de los cojones!")

else:
    print("Pues nada")