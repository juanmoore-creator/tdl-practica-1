import random
words = [
    "python",
    "programa",
    "variable",
    "funcion",
    "bucle",
    "cadena",
    "entero",
    "lista",
    ]
word = random.choice(words)
guessed = []
attempts = 6
print("¡Bienvenido al Ahorcado!")
print()
incorrectas = 0
while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)
    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        score = 6 - incorrectas
        print(f"¡Ganaste! Tu puntaje es: {score}")
        break
    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")  

    user_input = input("Ingresá una letra: ").lower()

    if len(user_input) != 1 or not user_input.isalpha():
        print("Entrada no válida")
        continue 

    letter = user_input # Asigno la entrada ya validada

    if letter in guessed:
        print("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(letter)
        incorrectas += 1
        attempts -= 1
        print("Esa letra no está en la palabra.")

    print()

else:
    print("Perdiste! El puntaje es: 0")
