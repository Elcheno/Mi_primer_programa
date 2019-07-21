#POKEMON v.2.1

#INICIACION#

import sys
n_pokemon = False
estado_pokemon = "live"
estado_pokemon_rival = "live"
hp_restante = False
estado = None

#Tus pokemons
#Charmander
charmander = ["CHARMANDER", 100, "BOLA FUEGO", 50, "COLMILLO IGNEO", 65]
#Bulbasur
bulbasur = ["BULBASUR", 105, "HOJA AFILADA", 40, "LATIGO CEPA", 62]

#Rival
nombre_rival = "Joselito"
#Pokemons Rival
#Onix
onix = ["ONIX", 120, "TUMBA ROCAS", 40]
#Pikachu
pikachu = ["PIKACHU", 95, "IMPACTRUENO", 70]
n_pokemon_rival = onix





#INICIO
print("Te has encontrado con {} un entrenador pokemon...".format(nombre_rival))
eleccion_1 = input("¿Quieres luchar contra el? [SI-NO]: ").upper()

#ELECCION DE POKEMON PART.1
if eleccion_1 == "SI":
    print("De acuerdo, el tiene 2 pokemons distintos y tu otros 2...")
    eleccion_2 = input("¿Quieres ver los stats de tu equipo? [SI-NO]: ").upper()

    #VISUALIZACION DE STATS
    if eleccion_2 == "SI":
        print("{} tiene {} de vida, su primer ataque {} hace {} de daño "
              "y su segundo ataque {} hace {} de daño.".format(charmander[0], charmander[1],
                                                              charmander[2], charmander[3],
                                                              charmander[4], charmander[5]))
        print("{} tiene {} de vida, su primer ataque {} hace {} de daño "
              "y su segundo ataque {} hace {} de daño.".format(bulbasur[0], bulbasur[1],
                                                              bulbasur[2], bulbasur[3],
                                                              bulbasur[4], bulbasur[5]))
    elif eleccion_2 == "NO":
        print("Esta bien, te veo confiado...")


    #ELECCION DE POKEMON PART.2
    eleccion_3 = input("¿Cual quieres utizar?: [CHARMANDER-BULBASUR]: ").upper()
    if eleccion_3 == "CHARMANDER":
        n_pokemon = charmander
    elif eleccion_3 == "BULBASUR":
        n_pokemon = bulbasur
    print("Gran eleccion has elegido a {} para comenzar...".format(n_pokemon[0]))

    #COMIENZA EL COMBATE
    print("De acuerdo vamos a comenzar, {} va a empezar con {}".format(nombre_rival, n_pokemon_rival[0]))
    print("¡Buena suerte! la necesitaras...")

    #BUCLE 1
    while estado_pokemon == "live" and estado_pokemon_rival == "live":
        menu = input("¿Cual va a ser tu accion? [LUCHAR-HUIR]: ").upper()
        if menu == "LUCHAR":
            eleccion_4 = input("¿Que ataque quieres que tu {} utilize? [{}-{}]: ".format(n_pokemon[0],
                                                                                        n_pokemon[2],
                                                                                        n_pokemon[4])).upper()
            if eleccion_4 == n_pokemon[2]:
                n_pokemon_rival[1] = n_pokemon_rival[1] - n_pokemon[3]
                hp_restante = n_pokemon[3]
            elif eleccion_4 == n_pokemon[4]:
                n_pokemon_rival[1] = n_pokemon_rival[1]- n_pokemon[5]
                hp_restante = n_pokemon[5]

            if n_pokemon_rival[1] < 0:
                hp_restante = hp_restante + n_pokemon_rival[1]
                n_pokemon_rival[1] = 0


            print("{} a utilizado {} y le a dejado a {} de HP a {}".format(n_pokemon[0],
                                                                           eleccion_4,
                                                                           n_pokemon_rival[1],
                                                                           n_pokemon_rival[0]))

            print("¡Eso significa que le has restado {} de HP!".format(hp_restante))

            if n_pokemon_rival[1] <= 0:
                estado_pokemon_rival = "death"
                print("¡Increible has debilitado al primer pokemon!")
                break





            print("Es turno del rival...")

            n_pokemon[1] -= n_pokemon_rival[3]
            hp_restante_rival = n_pokemon_rival[3]

            if n_pokemon[1] < 0:
                hp_restante_rival = hp_restante_rival + n_pokemon[1]
                n_pokemon[1] = 0

            print("{} ha utizado {} y ha dejado a tu {} a {} de HP".format(n_pokemon_rival[0],
                                                                           n_pokemon_rival[2],
                                                                           n_pokemon[0],
                                                                           n_pokemon[1]))
            print("¡Eso significa que te ha restado {} de HP!".format(hp_restante_rival))

            if n_pokemon[1] <= 0:
                estado_pokemon = "death"
                break
        elif menu == "HUIR":
            print("¡Has huido!")
            break


    if estado_pokemon == "death":
        if n_pokemon == charmander:
            n_pokemon = bulbasur
        elif n_pokemon == bulbasur:
            n_pokemon = charmander
    elif estado_pokemon_rival == "death":
        n_pokemon_rival = pikachu
########################################################################################################################
    estado_pokemon = "live"
    estado_pokemon_rival = "live"

    print("¡Ahora {} ha sacado a su segundo pokemon un {}!".format(nombre_rival, n_pokemon_rival[0]))

    eleccion_5 = input("¿Quieres cambiar de pokemon? [SI-NO]: ").upper()
    if eleccion_5 == "SI":
        if n_pokemon == charmander:
            n_pokemon = bulbasur
        elif n_pokemon == bulbasur:
            n_pokemon = charmander

    while estado_pokemon == "live" and estado_pokemon_rival == "live":
        if menu == "HUIR":
            break
        menu_2 = input("¿Cual va a ser tu accion? [LUCHAR-HUIR]: ").upper()
        if menu == "LUCHAR":
            eleccion_5 = input("¿Que ataque quieres que tu {} utilize? [{}-{}]: ".format(n_pokemon[0],
                                                                                        n_pokemon[2],
                                                                                        n_pokemon[4])).upper()
            if eleccion_5 == n_pokemon[2]:
                n_pokemon_rival[1] = n_pokemon_rival[1] - n_pokemon[3]
                hp_restante = n_pokemon[3]
            elif eleccion_5 == n_pokemon[4]:
                n_pokemon_rival[1] = n_pokemon_rival[1] - n_pokemon[5]
                hp_restante = n_pokemon[5]

            if n_pokemon_rival[1] < 0:
                hp_restante = hp_restante + n_pokemon_rival[1]
                n_pokemon_rival[1] = 0

        print("{} a utilizado {} y le a dejado a {} de HP a {}".format(n_pokemon[0],
                                                                       eleccion_5,
                                                                       n_pokemon_rival[1],
                                                                       n_pokemon_rival[0]))
        if n_pokemon_rival[1] <= 0:
            estado_pokemon_rival = "death"
            print("¡Increible has debilitado al segundo pokemon!")
            estado = "win"
            break
        print("Es turno del rival...")

        n_pokemon[1] -= n_pokemon_rival[3]
        hp_restante_rival = n_pokemon_rival[3]

        if n_pokemon[1] < 0:
            hp_restante_rival = hp_restante_rival + n_pokemon[1]
            n_pokemon[1] = 0

        print("{} ha utizado {} y ha dejado a tu {} a {} de HP".format(n_pokemon_rival[0],
                                                                       n_pokemon_rival[2],
                                                                       n_pokemon[0],
                                                                       n_pokemon[1]))
        print("¡Eso significa que te ha restado {} de HP!".format(hp_restante_rival))

        if n_pokemon[1] <= 0:
            print("¡Te han debilitado un pokemon, aprendete la tabla de tipos!")
            if n_pokemon == charmander:
                n_pokemon = bulbasur
            elif n_pokemon == bulbasur:
                n_pokemon = charmander
            print("Bueno no importa aun tiene a tu segundo pokemon {}".format(n_pokemon[0]))
            print("Esta bien ahora es tu turno...")

        elif menu_2 == "HUIR":
            print("¡Has huido!")
            break

    if estado == "win":
        print("¡Eso significa que has ganado increible!")
        print("¡FELICIDADES!")

elif eleccion_1 == "NO":
    print("¡Has huido!")

    #FIN-FIN-FIN...





