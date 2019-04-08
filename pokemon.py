# Eligiendo el pokemon
pokemon_elegido = input("¿Contra que pokemon quieres luchar?  (Squirtle / Charmander / Bulbasur)").upper()

print("¡Increible te vas a enfrentar a {}!".format(pokemon_elegido))

# Stats
#Tu Pokemon
nombre_pokemon = "Pikachu"
vida_pokemon = 100
ataque_one = "CHISPAZO"
ataque_two = "BOLA VOLTIO"
ataque_uno = 10
ataque_dos = 12
dano_pokemon = 0#Este no tocar

#Enemigo
dano_enemigo = 0#Este no tocar
vida_enemigo = 0#Este no tocar


#Stats enemigos
if pokemon_elegido == "SQUIRTLE":
    vida_enemigo = 90
    dano_enemigo = 8
elif pokemon_elegido == "CHARMANDER":
    vida_enemigo = 80
    dano_enemigo = 7
elif pokemon_elegido == "BULBASUR":
    vida_enemigo = 100
    dano_enemigo = 9

# Empieza el combate

print("¡Ya empieza el combate y tu y tu {} empiezais atacando!".format(nombre_pokemon))

while vida_pokemon > 0 and vida_enemigo > 0:

    ataque_elegido = input("¿Que ataque quieres utilizar?  (Chispazo / Bola voltio)").upper()

    # Tus ataques y su respectivo daño

    if ataque_elegido == ataque_one:
        dano_pokemon = ataque_uno
    elif ataque_elegido == ataque_two:
        dano_pokemon = ataque_dos

    print("Has utilizado {}".format(ataque_elegido))

    vida_enemigo -= dano_pokemon

    print("Has dejado al {} enemigo a {} de HP".format(pokemon_elegido, vida_enemigo))

    vida_pokemon -= dano_enemigo

    print("{} enemigo ha utilizado arañazo y te ha echo {} de daño".format(pokemon_elegido, dano_enemigo))

    print("Tu {} esta a {} de HP".format(nombre_pokemon, vida_pokemon))

    # Ha terminado el combate

print("El combate ha terminado")

if vida_pokemon > 0:
    print("Tu y tu {} habeis ganado, felicidades".format(nombre_pokemon))
elif vida_enemigo > 0:
    print("Lo siento habeis perdido vuelve a intentarlo...")

    # FIN