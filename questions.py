import random

# Diccionario de categorías
categorias = {
    "Programación": ["python", "variable", "funcion", "bucle"],
    "Tipos de Datos": ["entero", "cadena", "lista", "booleano"],
    "Herramientas": ["git", "github", "terminal", "editor"]
}

print("¡Bienvenido al Ahorcado!")

# Bucle principal para permitir cambiar de categoría si terminan las palabras
while True:
    print("\nCategorías disponibles:")
    for cat in categorias.keys():
        print(f"- {cat}")

    seleccion = input("Elegí una categoría (se debe escribir el nombre exacto): ")
    while seleccion not in categorias:
        seleccion = input("Categoría no válida. Elegí una de la lista: ")

    # Obtenemos la lista de palabras de la categoría elegida
    palabras_categoria = categorias[seleccion]
    
    # random.sample para desordenar las palabras sin repetir ninguna
    palabras_mezcladas = random.sample(palabras_categoria, len(palabras_categoria))

    # Bucle de rondas (recorre las palabras desordenadas una por una)
    for word in palabras_mezcladas:
        print(f"\n--- NUEVA RONDA: Categoría '{seleccion}' ---")
        
        guessed = []
        attempts = 6
        incorrectas = 0
        
        # Bucle de una partida individual
        while attempts > 0:
            # Mostrar progreso: letras adivinadas y guiones para las que faltan
            progress = ""
            for letter in word:
                if letter in guessed:
                    progress += letter + " "
                else:
                    progress += "_ "
            print("\nPalabra:", progress)
            
            # Verificar si el jugador ya adivinó la palabra completa
            if "_" not in progress:
                score = 6 - incorrectas
                print(f"¡Ganaste! Tu puntaje es: {score}")
                break
                
            print(f"Intentos restantes: {attempts}")
            print(f"Letras usadas: {', '.join(guessed)}")  

            # Validación de entrada
            user_input = input("Ingresá una letra: ").lower()

            if len(user_input) != 1 or not user_input.isalpha():
                print("Entrada no válida")
                continue 

            letter = user_input # Asigno la entrada ya validada

            # Lógica de aciertos y errores
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

        # Condición de derrota (si el bucle while termina por quedarse sin intentos)
        if attempts == 0:
            print(f"\nPerdiste! La palabra era: '{word}'. El puntaje es: 0")

        # Preguntar si desea jugar la siguiente ronda
        continuar = input("\n¿Querés jugar otra ronda con la siguiente palabra? (s/n): ").lower()
        if continuar != 's':
            break # Rompe el bucle de palabras (for)

    else:
        print(f"\n¡Completaste todas las palabras de la categoría '{seleccion}'!")

    # Preguntar si desea reiniciar el juego por completo (elegir nueva categoría)
    reiniciar = input("¿Querés elegir otra categoría y seguir jugando? (s/n): ").lower()
    if reiniciar != 's':
        print("¡Gracias por jugar! Hasta luego.")
        break 